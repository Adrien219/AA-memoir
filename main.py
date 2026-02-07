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
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialisation
vision = VisionEngine()
arduino = ArduinoBridge()

def get_full_system_metrics():
    """Récupère l'intégralité des performances machine"""
    metrics = {
        "cpu_usage": psutil.cpu_percent(),
        "cpu_freq": round(psutil.cpu_freq().current if psutil.cpu_freq() else 0, 0),
        "ram_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
        "boot_time": time.strftime("%H:%M:%S", time.localtime(psutil.boot_time())),
        "pi_temp": 0,
        "os": platform.system()
    }
    if platform.system() == "Linux":
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                metrics["pi_temp"] = round(int(f.read()) / 1000, 1)
        except: pass
    return metrics

def generate_frames():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

    while True:
        t_start = time.perf_counter()
        success, frame = cap.read()
        if not success: break

        # 1. IA : Inférence
        results = vision.model(frame, stream=True, conf=0.4, verbose=False, imgsz=320)
        detections = []
        max_conf = 0
        
        for r in results:
            frame = r.plot()
            for box in r.boxes:
                conf = float(box.conf[0])
                label = vision.model.names[int(box.cls[0])]
                detections.append(f"{label} ({int(conf*100)}%)")
                if conf > max_conf: max_conf = conf

        # 2. Performances IA
        t_end = time.perf_counter()
        latence = round((t_end - t_start) * 1000, 2)
        precision = round(max_conf * 100, 1)

        # 3. Récupération données
        arduino_data = arduino.read_data()
        sys_data = get_full_system_metrics()

        print("\n" + "="*60)
        print(f" 🖥️  SYSTEM [{sys_data['os']}] | RTC: {arduino_data.get('time', 'N/A')}")
        print("="*60)
        print(f"[👁️  IA] Latence: {latence}ms | Précision: {precision}%")
        print(f"[👁️  IA] Objets: {', '.join(detections) if detections else 'Aucun'}")
        print(f"[💻 HW] CPU: {sys_data['cpu_usage']}% | RAM: {sys_data['ram_usage']}% | Disque: {sys_data['disk_usage']}%")
        
        lum_status = "SOMBRE" if arduino_data.get('lum') == 1 else "LUMINEUX"
        print(f"[🌡️ ENV] Temp: {arduino_data.get('temp_ext')}°C | Lum: {lum_status} | Dist: {arduino_data.get('dist')}cm")
        
        print(f"[🎮 INT] Joy: X={arduino_data.get('joy_x')} Y={arduino_data.get('joy_y')} | Obs IR: {'DANGER' if arduino_data.get('obs')==0 else 'OK'}")
        print("="*60 + "\n")

        # 4. Envoi Web
        payload = {
            "sensors": arduino_data,
            "perf_ia": {"latence": latence, "precision": precision, "objects": detections},
            "perf_sys": sys_data
        }
        socketio.emit('full_system_update', payload)

        # 5. Encodage Vidéo
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    import logging
    logging.getLogger('werkzeug').setLevel(logging.ERROR)
    print(f"🚀 Serveur lancé sur http://localhost:5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)