import subprocess
import json
import time
import threading
import sys
import os
from paho.mqtt import client as mqtt_client

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from bridge import ArduinoBridge
except ImportError:
    print("❌ Erreur : bridge.py introuvable.")
    sys.exit(1)

class SHOS_Backbone:
    def __init__(self):
        self.client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2, "BACKBONE_MASTER")
        # Augmenter la taille du buffer pour les images
        self.client.max_inflight_messages_set(20)
        
        try:
            self.client.connect("localhost", 1883, 60)
            print("📡 Backbone : Liaison MQTT établie")
        except:
            print("❌ Backbone : Broker Mosquitto injoignable")
            sys.exit(1)

        self.arduino = ArduinoBridge(port='/dev/ttyUSB0')
        self.running = True

    def start_camera(self):
        """ Capture et découpe proprement le flux MJPEG """
        print("📸 Backbone : Flux caméra MJPEG activé...")
        cmd = [
            'libcamera-vid', '-t', '0', '--inline', '--width', '640', 
            '--height', '480', '--codec', 'mjpeg', '-n', '--flush', '-o', '-'
        ]
        
        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            buffer = b''
            while self.running:
                chunk = proc.stdout.read(4096)
                if not chunk:
                    break
                
                buffer += chunk
                # Recherche des délimiteurs JPEG (Start of Image et End of Image)
                start = buffer.find(b'\xff\xd8')
                end = buffer.find(b'\xff\xd9')
                
                if start != -1 and end != -1 and end > start:
                    jpg = buffer[start:end+2]
                    buffer = buffer[end+2:]
                    # Publication de l'image complète uniquement
                    self.client.publish("helmet/camera/raw", jpg, qos=0)
        except Exception as e:
            print(f"❌ Erreur Caméra : {e}")

    def hardware_loop(self):
        while self.running:
            data = self.arduino.read_data()
            if data:
                self.client.publish("helmet/sensors/raw", json.dumps(data))
            time.sleep(0.1)

    def run(self):
        print("\n🚀 === S.H.O.S BACKBONE ONLINE ===")
        threading.Thread(target=self.start_camera, daemon=True).start()
        threading.Thread(target=self.hardware_loop, daemon=True).start()
        try:
            while True: time.sleep(1)
        except KeyboardInterrupt:
            self.running = False

if __name__ == "__main__":
    os.system("sudo chmod 666 /dev/ttyUSB0 2>/dev/null")
    SHOS_Backbone().run()