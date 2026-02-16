import eventlet
eventlet.monkey_patch()

import sys
import os
import time
import json
import psutil
from flask import Flask, render_template, Response, jsonify, request
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt

# Ajout du dossier parent pour trouver config_manager.py et config.json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config_manager import ConfigManager

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*")
cm = ConfigManager()

# Variable globale pour le flux vidéo
last_frame = None

# --- MONITORING SYSTÈME ---
def background_system_monitor():
    while True:
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        temp = 0
        try:
            # Lecture de la température du Raspberry Pi
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                temp = int(f.read()) / 1000
        except: 
            temp = 0
            
        socketio.emit('sys_update', {
            'cpu': cpu, 
            'ram': ram, 
            'temp': round(temp, 1),
            'bat': 85, 
            'wifi': 90
        })
        socketio.sleep(2)

# --- CONFIGURATION MQTT ---
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"📡 MQTT: Connecté. Écoute des capteurs et de la caméra...")
    client.subscribe([("helmet/sensors/raw", 0), ("helmet/camera/raw", 0)])

def on_message(client, userdata, msg):
    global last_frame
    try:
        # 1. Données des capteurs Arduino
        if msg.topic == "helmet/sensors/raw":
            data = json.loads(msg.payload.decode())
            socketio.emit('sensor_update', data)
        
        # 2. Flux vidéo venant du Backbone
        elif msg.topic == "helmet/camera/raw":
            last_frame = msg.payload
            
    except Exception as e:
        print(f"⚠️ Erreur décodage MQTT: {e}")

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect("localhost", 1883, 60)
mqtt_client.loop_start()

# --- ROUTES DE NAVIGATION ---

@app.route('/')
def home():
    """Affiche la page d'accueil (Sélection des profils)"""
    config = cm.load_config()
    profiles = config.get('profiles', {})
    return render_template('home.html', profiles=profiles)

@app.route('/ui')
def user_interface():
    """Affiche l'interface utilisateur opérationnelle (HUD)"""
    config = cm.load_config()
    current_id = config.get('current_active_profile', 'exploration')
    profile_data = config['profiles'].get(current_id, {})
    return render_template('user_interface.html', profile=profile_data)

@app.route('/diag')
def diagnostic():
    """Affiche le panneau de diagnostic technique"""
    config = cm.load_config()
    current_id = config.get('current_active_profile', 'exploration')
    profile_data = config['profiles'].get(current_id, {})
    return render_template('diagnostic.html', profile=profile_data)

@app.route('/create_profile')
def create_profile():
    """Affiche le Profile Manager"""
    config = cm.load_config()
    modules = config.get('available_modules', {})
    return render_template('profile_manager.html', modules=modules)

# --- ROUTES API ---

@app.route('/activate/<profile_id>')
def activate(profile_id):
    if cm.activate_profile(profile_id):
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 400

@app.route('/video_feed')
def video_feed():
    """Route pour le streaming MJPEG"""
    def gen_frames():
        global last_frame
        while True:
            if last_frame:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + last_frame + b'\r\n')
            eventlet.sleep(0.04) # Environ 25 FPS
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@socketio.on('connect')
def handle_connect():
    socketio.start_background_task(background_system_monitor)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)