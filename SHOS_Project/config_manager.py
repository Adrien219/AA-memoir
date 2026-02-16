import json
import os
import paho.mqtt.client as mqtt

class ConfigManager:
    def __init__(self, config_path=None):
        if config_path is None:
            # Trouve le chemin absolu du config.json à côté du script manager
            base_dir = os.path.dirname(os.path.abspath(__file__))
            self.config_path = os.path.join(base_dir, 'config.json')
        else:
            self.config_path = config_path
        self.mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "CONFIG_MANAGER")
        
        # Connexion MQTT pour piloter les modules
        try:
            self.mqtt_client.connect("localhost", 1883, 60)
            self.mqtt_client.loop_start()
        except:
            print("⚠️ ConfigManager : Broker MQTT injoignable.")

    def load_config(self):
        """Lit le fichier JSON"""
        if not os.path.exists(self.config_path):
            return None
        with open(self.config_path, 'r') as f:
            return json.load(f)

    def save_config(self, data):
        """Enregistre les modifications dans le JSON"""
        with open(self.config_path, 'w') as f:
            json.dump(data, f, indent=4)

    def activate_profile(self, profile_id):
        """La fonction clé : lance un profil et ses modules associés"""
        config = self.load_config()
        if not config or profile_id not in config['profiles']:
            print(f"❌ Profil {profile_id} inconnu.")
            return False

        # 1. On coupe tout avant de changer (Un seul profil à la fois)
        self.mqtt_client.publish("helmet/system/reset", "true")

        # 2. On récupère les infos du nouveau profil
        profile = config['profiles'][profile_id]
        main_mod = profile['main_module']
        others = profile['secondary_modules']

        print(f"🚀 Activation du profil : {profile['name']}")

        # 3. On active le module principal
        self.mqtt_client.publish(f"helmet/modules/{main_mod}", "start_main")

        # 4. On active les modules secondaires
        for mod in others:
            self.mqtt_client.publish(f"helmet/modules/{mod}", "start_secondary")

        # 5. On met à jour l'état actuel dans le JSON
        config['current_active_profile'] = profile_id
        self.save_config(config)
        return True

# Test rapide si on lance le script seul
if __name__ == "__main__":
    cm = ConfigManager()
    cm.activate_profile("default")