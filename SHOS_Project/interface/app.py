import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template, Response
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
import json
import psutil # Pour le CPU/RAM

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*")

# Structure de données synchronisée avec l'Arduino
system_data = {
    "perf_sys": {"cpu_usage": 0, "ram_usage": 0, "pi_temp": 0},
    "sensors": {
        "dist": 0, "gas": 0, "temp_ext": 0, "hum": 0, 
        "son": 0, "lum": 0, "joy_x": 512, "joy_y": 512, 
        "btn": 0, "obs": 1, "time": "00:00"
    },
    "perf_ia": {"latence": 0, "precision": 0, "objects": []}
}

last_frame = None

def on_message(client, userdata, msg):
    global last_frame, system_data
    if msg.topic == "helmet/camera/raw":
        last_frame = msg.payload
    else:
        try:
            payload = json.loads(msg.payload.decode())
            # Mise à jour intelligente des dictionnaires
            if "sensors" in msg.topic:
                system_data["sensors"].update(payload)
            elif "vision" in msg.topic:
                system_data["perf_ia"]["objects"] = payload.get("found", [])
            
            # Ajout des stats du Raspberry Pi
            system_data["perf_sys"]["cpu_usage"] = psutil.cpu_percent()
            system_data["perf_sys"]["ram_usage"] = psutil.virtual_memory().percent
            try:
                with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                    system_data["perf_sys"]["pi_temp"] = int(int(f.read()) / 1000)
            except: pass

            socketio.emit('full_system_update', system_data)
        except: pass

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.on_message = on_message
mqtt_client.connect("localhost", 1883, 60)
mqtt_client.subscribe([("helmet/camera/raw", 0), ("helmet/sensors/raw", 0), ("helmet/plugins/vision_objet/data", 0)])
mqtt_client.loop_start()

@app.route('/')
def index(): return render_template('hud.html')

def gen():
    while True:
        if last_frame:
            yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + last_frame + b'\r\n')
        eventlet.sleep(0.04)

@app.route('/video_feed')
def video_feed(): return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)