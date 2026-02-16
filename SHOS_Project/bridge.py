import serial
import json
import time
from paho.mqtt import client as mqtt_client

class ArduinoBridge:
    def __init__(self, port='/dev/ttyUSB0', baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        
        # Configuration MQTT (Norme v2)
        self.client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2, "BridgeArduino")
        try:
            self.client.connect("localhost", 1883, 60)
            print("✅ Bridge : Connecté au Broker MQTT")
        except:
            print("❌ Bridge : Échec connexion MQTT")

        # Connexion Série
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"✅ Bridge : Arduino connecté sur {self.port}")
        except:
            print(f"⚠️ Bridge : Impossible de trouver l'Arduino sur {self.port}")

    def read_data(self):
        if self.ser and self.ser.in_waiting > 0:
            try:
                line = self.ser.readline().decode('utf-8').strip()
                data = json.loads(line)
                return data
            except:
                return None
        return None