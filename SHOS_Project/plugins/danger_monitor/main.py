import paho.mqtt.client as mqtt
import json
import time

# --- CONFIGURATION DES TOPICS ---
TOPIC_SENSORS = "helmet/sensors/raw"
TOPIC_CONTROL = "helmet/plugins/danger_monitor/control"
TOPIC_GLOBAL = "helmet/plugins/control"
TOPIC_RESULTS = "helmet/plugins/danger_monitor/data"
TOPIC_VOICE = "helmet/plugins/voice_assistant/control" # Pour parler
TOPIC_ARDUINO_CMD = "helmet/arduino/cmd" # Pour retour physique

class DangerMonitor:
    def __init__(self):
        print("🛡️ [DANGER] Initialisation du moniteur de sécurité...")
        self.active = False  
        self.dist_threshold = 30  # cm
        self.gas_threshold = 400   
        self.last_alert_time = 0   # Pour éviter de spammer les alertes vocales
        
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "PLUGIN_DANGER")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        
        try:
            self.client.connect("localhost", 1883, 60)
        except Exception as e:
            print(f"❌ [DANGER] Erreur MQTT : {e}")

    def on_connect(self, client, userdata, flags, rc, properties):
        if rc == 0:
            print("✅ [DANGER] Connecté. Surveillance prête.")
            client.subscribe([
                (TOPIC_SENSORS, 0),
                (TOPIC_CONTROL, 0),
                (TOPIC_GLOBAL, 0)
            ])

    def trigger_haptic_feedback(self, level):
        """ Envoie un ordre à l'Arduino pour réagir physiquement """
        cmd = {"action": "alert", "level": level}
        self.client.publish(TOPIC_ARDUINO_CMD, json.dumps(cmd))

    def send_voice_alert(self, message):
        """ Envoie un message au plugin Voice Assistant """
        current_time = time.time()
        # On limite à une alerte vocale toutes les 5 secondes
        if current_time - self.last_alert_time > 5:
            msg = {"action": "say", "text": message}
            self.client.publish(TOPIC_VOICE, json.dumps(msg))
            self.last_alert_time = current_time

    def on_message(self, client, userdata, msg):
        try:
            # 1. GESTION DU PROFIL
            if msg.topic in [TOPIC_CONTROL, TOPIC_GLOBAL]:
                command = json.loads(msg.payload.decode())
                action = command.get("action")
                
                if action == "start":
                    self.active = True
                    print("🚀 [DANGER] Surveillance ACTIVÉE")
                    self.send_voice_alert("Système de sécurité activé")
                elif action in ["stop", "stop_all"]:
                    self.active = False
                    print("😴 [DANGER] Surveillance en PAUSE")
                return

            # 2. ANALYSE DES RISQUES
            if self.active and msg.topic == TOPIC_SENSORS:
                data = json.loads(msg.payload.decode())
                alerts = []
                
                # Vérification Obstacle
                dist = data.get("dist", 999)
                if dist < self.dist_threshold:
                    alerts.append({"type": "OBSTACLE", "value": dist, "level": "CRITICAL"})
                    self.send_voice_alert(f"Attention, obstacle à {dist} centimètres")
                
                # Vérification Gaz
                gas = data.get("gas", 0)
                if gas > self.gas_threshold:
                    alerts.append({"type": "GAS", "value": gas, "level": "DANGER"})
                    self.send_voice_alert("Alerte. Concentration de gaz anormale")

                # Si alerte : Publication pour le HUD et Feedback physique
                if alerts:
                    print(f"⚠️ [ALERT] Risques détectés : {alerts}")
                    
                    # Publication pour l'interface web (HUD)
                    self.client.publish(TOPIC_RESULTS, json.dumps({
                        "plugin": "danger_monitor",
                        "alerts": alerts,
                        "timestamp": time.time()
                    }))
                    
                    # Feedback physique (Vibreur/LED via Bridge/Arduino)
                    self.trigger_haptic_feedback("high")

        except Exception as e:
            print(f"❌ [DANGER] Erreur traitement : {e}")

    def run(self):
        self.client.loop_forever()

if __name__ == "__main__":
    monitor = DangerMonitor()
    monitor.run()