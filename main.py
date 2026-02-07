import eventlet
eventlet.monkey_patch()

import cv2
import psutil
import platform
import time
import json
import os
from flask import Flask, render_template, Response
from flask_socketio import SocketIO
from vision import VisionEngine
from bridge import ArduinoBridge

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# --- CONFIGURATION ---
# On force le nouveau port détecté : /dev/ttyUSB1
PORT_ARDUINO = '/dev/ttyUSB1'

vision = VisionEngine()
arduino = ArduinoBridge(port=PORT_ARDUINO)

def get_full_system_metrics():
    metrics = {
        "cpu_usage": psutil.cpu_percent(),
        "ram_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
        "pi_temp": 0,
        "os": platform.system()
    }
    if platform.system() == "Linux":
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                metrics["pi_temp"] = round(int(f.read()) / 1000, 1)
        except: pass
    return metrics

def background_task():
    """ Lit les capteurs et envoie au web en continu (indépendant de la vidéo) """
    print("🛰️  Démarrage de la tâche de fond (Capteurs)...")
    while True:
        arduino_data = arduino.read_data()
        sys_data = get_full_system_metrics()
        
        # --- AFFICHAGE TERMINAL (DEBUG) ---
        dist = arduino_data.get('dist', '??')
        temp = arduino_data.get('temp_ext', '??')
        print(f"[LIVE] Distance: {dist}cm | Temp Ext: {temp}°C | CPU: {sys_data['cpu_usage']}%")
        
        # Envoi au HUD
        payload = {
            "sensors": arduino_data,
            "perf_ia": {"latence": 0, "precision": 0, "objects": []}, # Sera complété par la vidéo
            "perf_sys": sys_data
        }
        socketio.emit('full_system_update', payload)
        
        eventlet.sleep(0.5) # Mise à jour 2 fois par seconde

def generate_frames():
    cap = cv2.VideoCapture(0)
    # Optimisation résolution pour Raspberry Pi
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Inférence IA ultra-légère
        results = vision.model(frame, stream=True, conf=0.4, verbose=False, imgsz=160)
        
        detections = []
        for r in results:
            frame = r.plot()
            for box in r.boxes:
                label = vision.model.names[int(box.cls[0])]
                detections.append(label)

        # Envoi partiel pour mettre à jour la liste des objets détectés sur le HUD
        socketio.emit('full_system_update', {
            "sensors": {}, # Les capteurs sont gérés par la tâche de fond
            "perf_ia": {"objects": detections, "latence": 0, "precision": 0},
            "perf_sys": {}
        })

        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
        eventlet.sleep(0.01)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # On autorise l'accès au port ttyUSB1 avant de lancer
    os.system(f"sudo chmod 666 {PORT_ARDUINO}")
    
    print(f"\n🚀 MISSION CONTROL EN LIGNE")
    print(f"📡 Arduino : {PORT_ARDUINO}")
    
    # Lancement de la tâche de fond
    eventlet.spawn(background_task)
    
    print(f"🔗 HUD : http://localhost:5000\n")
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)