import paho.mqtt.client as mqtt
import json
import os
import time

# --- CONFIGURATION DES TOPICS ---
TOPIC_CONTROL = "helmet/plugins/voice_assistant/control"
TOPIC_GLOBAL = "helmet/plugins/control"
# On écoute les sorties des autres plugins pour les annoncer
TOPIC_VISION = "helmet/plugins/vision_objet/data"
TOPIC_DANGER = "helmet/plugins/danger_monitor/data"

class VoiceAssistant:
    def __init__(self):
        print("🗣️ [VOICE] Initialisation de l'assistant vocal...")
        self.active = False
        
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "PLUGIN_VOICE")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        
        try:
            self.client.connect("localhost", 1883, 60)
        except Exception as e:
            print(f"❌ [VOICE] Erreur MQTT : {e}")

    def speak(self, text):
        """ Utilise espeak pour parler sans bloquer le reste du code """
        if self.active:
            print(f"🎙️ Assistant dit : {text}")
            # Commande système pour faire parler le Pi (français)
            os.system(f'espeak -v fr "{text}" &')

    def on_connect(self, client, userdata, flags, rc, properties):
        if rc == 0:
            print("✅ [VOICE] Assistant prêt et connecté.")
            client.subscribe([
                (TOPIC_CONTROL, 0),
                (TOPIC_GLOBAL, 0),
                (TOPIC_VISION, 0),
                (TOPIC_DANGER, 0)
            ])

    def on_message(self, client, userdata, msg):
        try:
            # 1. GESTION DU PROFIL
            if msg.topic in [TOPIC_CONTROL, TOPIC_GLOBAL]:
                command = json.loads(msg.payload.decode())
                action = command.get("action")
                
                if action == "start":
                    self.active = True
                    self.speak("Assistant vocal activé")
                elif action in ["stop", "stop_all"]:
                    self.active = False
                    print("😴 [VOICE] Assistant en PAUSE")
                return

            # 2. RÉACTION AUX DONNÉES (Seulement si actif)
            if not self.active:
                return

            data = json.loads(msg.payload.decode())

            # Si le module DANGER détecte quelque chose
            if msg.topic == TOPIC_DANGER:
                for alert in data.get("alerts", []):
                    if alert["type"] == "OBSTACLE":
                        self.speak("Attention obstacle proche")
                    elif alert["type"] == "GAS":
                        self.speak("Alerte gaz détectée")

            # Si le module VISION détecte un objet
            elif msg.topic == TOPIC_VISION:
                objets = data.get("found", [])
                if objets:
                    texte = "Je vois : " + ", ".join(objets)
                    self.speak(texte)

        except Exception as e:
            print(f"❌ [VOICE] Erreur : {e}")

    def run(self):
        self.client.loop_forever()

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()