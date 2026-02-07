import serial
import json

class ArduinoBridge:
    def __init__(self, port='COM4', baudrate=9600):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=0.1)
            print(f"✅ Arduino connecté sur {port}")
        except Exception as e:
            self.ser = None
            print(f"❌ Erreur connexion Arduino : {e}")

    def read_data(self):
        """Lit les données JSON envoyées par l'Arduino"""
        if self.ser and self.ser.is_open and self.ser.in_waiting > 0:
            try:
                line = self.ser.readline().decode('utf-8').strip()
                if line.startswith('{') and line.endswith('}'):
                    return json.loads(line)
            except Exception:
                return {}
        return {}