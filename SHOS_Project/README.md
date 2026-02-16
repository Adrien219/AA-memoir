Copie ce code dans ton fichier main.py.

Assure-toi d'être dans ton environnement avec source ~/venv/bin/activate

Lance avec python3 main.py

Ouvre ton navigateur sur http://localhost:5000


./start_shos.sh







#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <RTClib.h>
#include <DHT.h>

// --- CONFIGURATION PINS ---
#define TRIG_PIN 2
#define ECHO_PIN 3
#define JOY_BTN 4
#define DHT_PIN 5
#define FISH_PIN 6  // Capteur obstacle IR
#define LIGHT_PIN 7
#define BUZZER_PIN 9
#define VIBREUR_PIN 10
#define RGB_R 11
#define RGB_G 12
#define RGB_B 13
#define JOY_X A0
#define JOY_Y A1
#define GAS_PIN A2
#define SOUND_PIN A3

// --- OBJETS ---
DHT dht(DHT_PIN, DHT11);
LiquidCrystal_I2C lcd(0x27, 16, 2); // Adresse I2C 0x27 ou 0x3F
RTC_DS3231 rtc;

void setup() {
  Serial.begin(115200);
  
  // Initialisation capteurs/actuateurs
  dht.begin();
  lcd.init();
  lcd.backlight();
  if (!rtc.begin()) { /* RTC non trouvé */ }

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(JOY_BTN, INPUT_PULLUP);
  pinMode(FISH_PIN, INPUT);
  pinMode(LIGHT_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(VIBREUR_PIN, OUTPUT);
  pinMode(RGB_R, OUTPUT);
  pinMode(RGB_G, OUTPUT);
  pinMode(RGB_B, OUTPUT);

  lcd.setCursor(0,0);
  lcd.print("SmartGlasses OS");
}

void loop() {
  // 1. DISTANCE ULTRASON
  digitalWrite(TRIG_PIN, LOW); delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH); delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long dist = pulseIn(ECHO_PIN, HIGH) * 0.034 / 2;

  // 2. ENVIRONNEMENT
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  int gas = analogRead(GAS_PIN);
  int sound = analogRead(SOUND_PIN);
  int ir_obs = digitalRead(FISH_PIN); // 0 si obstacle, 1 si rien
  int light = digitalRead(LIGHT_PIN); 

  // 3. JOYSTICK
  int x = analogRead(JOY_X);
  int y = analogRead(JOY_Y);
  int btn = !digitalRead(JOY_BTN); // Inversé car Pullup

  // 4. TEMPS (RTC)
  DateTime now = rtc.now();

  // 5. AFFICHAGE LCD (Local)
  lcd.setCursor(0,1);
  lcd.print(dist); lcd.print("cm ");
  lcd.print(t, 0); lcd.print("C  ");
  lcd.print(now.hour()); lcd.print(":"); lcd.print(now.minute());

  // 6. LOGIQUE DE SÉCURITÉ (Feedback direct)
  if (gas > 400 || dist < 15) {
    digitalWrite(VIBREUR_PIN, HIGH);
    digitalWrite(RGB_R, HIGH);
    digitalWrite(RGB_B, LOW);
  } else {
    digitalWrite(VIBREUR_PIN, LOW);
    digitalWrite(RGB_R, LOW);
    digitalWrite(RGB_G, HIGH); // Vert si tout va bien
  }

  // 7. ENVOI JSON VERS PYTHON
  Serial.print("{");
  Serial.print("\"dist\":"); Serial.print(dist);
  Serial.print(",\"gas\":"); Serial.print(gas);
  Serial.print(",\"temp_ext\":"); Serial.print(isnan(t) ? 0 : t);
  Serial.print(",\"hum\":"); Serial.print(isnan(h) ? 0 : h);
  Serial.print(",\"son\":"); Serial.print(sound);
  Serial.print(",\"lum\":"); Serial.print(light);
  Serial.print(",\"joy_x\":"); Serial.print(x);
  Serial.print(",\"joy_y\":"); Serial.print(y);
  Serial.print(",\"btn\":"); Serial.print(btn);
  Serial.print(",\"obs\":"); Serial.print(ir_obs);
  Serial.print(",\"time\":\""); Serial.print(now.hour()); Serial.print(":"); Serial.print(now.minute()); Serial.print("\"");
  Serial.println("}");

  delay(500);





























PROJET : S.H.O.S (Smart Helmet Operating System)
Système d'Exploitation Modulaire pour Casque de Réalité Augmentée Industriel & Assistance

1. 🎯 Vision et Objectifs
Le projet consiste à concevoir un casque intelligent intégral (type VR/AR pass-through) autonome. Contrairement à des lunettes légères, ce casque embarque une puissance de calcul complète et une multitude de capteurs pour des environnements complexes (mines, usines) ou pour l'assistance au handicap.

Philosophie : Le système fonctionne comme un OS (Système d'Exploitation). Il ne fait rien tout seul, mais il fournit les ressources (vidéo, capteurs, réseau) à des Plugins que l'utilisateur active selon son Profil (Mineur, Navigation, Maintenance, etc.).

2. 🏗️ Architecture Matérielle (Le Casque)
Le casque est un dispositif autonome qui intègre l'informatique, la vision et l'énergie.

A. Le Cœur (Unités de Calcul)
Cerveau Principal (Master) : Raspberry Pi 4 ou 5.

Rôle : Héberge l'OS, le Backbone, le serveur MQTT, le traitement vidéo et l'IA.

OS : Raspberry Pi OS (Bookworm).

Cerveau Sensoriel (Slave) : Arduino (Nano/Uno) connecté en USB (/dev/ttyUSB0).

Rôle : Interface bas niveau. Il lit les capteurs analogiques/numériques en temps réel et envoie les données brutes à la Pi via Série (Serial).

B. Les Organes (Périphériques)
Vision : Module Caméra Pi (Connecteur CSI) ou Webcam USB grand angle.

Affichage (HUD) : Écran interne du casque (HDMI ou DSI) affichant l'interface web en plein écran (Mode Kiosque).

Capteurs (Liste évolutive connectée à l'Arduino) :

Distance (Ultrasons/LiDAR) : Pour la détection d'obstacles.

Environnement : DHT11/22 (Température/Humidité), MQ-x (Gaz toxiques/Fumée).

Position : Module GPS (Latitude/Longitude).

Mouvement : Accéléromètre/Gyroscope (Orientation de la tête).

Énergie : Power Bank haute capacité (5V/3A min) intégrée à l'arrière du casque (contrepoids).

3. 🧠 Architecture Logicielle (Le Backbone)
C'est une architecture Micro-Services basée sur un bus de données.

A. Le Concept "Backbone" (Colonne Vertébrale)
Le script backbone.py est le seul maître à bord. Il se lance au démarrage.

Il ne réfléchit pas. (Pas d'IA).

Il fournit. Il capture le flux vidéo et les données Arduino.

Il distribue. Il publie tout sur le réseau local interne via MQTT.

B. Le Protocole de Communication (MQTT)
Le système nerveux du casque est le protocole MQTT (Message Queuing Telemetry Transport). Tout passe par là via un "Broker" (Mosquitto) installé sur la Pi.

Structure des "Topics" (Canaux de discussion) :

helmet/system/control : Commandes (Changer de profil, Arrêt d'urgence).

helmet/camera/raw : Flux vidéo brut (MJPEG binaire).

helmet/sensors/all : JSON contenant toutes les valeurs capteurs {temp: 24, gaz: 10, dist: 150}.

helmet/plugins/[nom_du_plugin]/data : Résultats des modules (ex: helmet/plugins/vision/detections).

4. 🧩 Le Système de Plugins & Profils
Le système est "agnostique". Il ne sait pas ce qu'il doit faire tant qu'un Profil n'est pas chargé.

A. Dossier /plugins
Chaque fonctionnalité est un dossier indépendant.

Exemple : /plugins/vision_objet/

Contient main.py : S'abonne à helmet/camera/raw, charge YOLO, détecte, publie sur MQTT.

Contient widget.html : Code HTML/JS pour afficher le carré rouge sur l'écran.

B. Dossier /modeles
Stockage centralisé des cerveaux IA (yolov8n.pt, ocr_model.tflite, etc.). Les plugins viennent piocher ici.

C. Les Profils Utilisateurs (profiles.json)
C'est le fichier qui définit l'usage du casque.

Scénario 1 : Profil "Navigation (Aveugle)"

Modules activés : vision_objet, gps, audio_guide.

Comportement : Le casque ignore le capteur de gaz. Il lance l'IA de vision.

Scénario 2 : Profil "Industrie (Mineur)"

Modules activés : gaz_monitor, environment, remote_assist, flashlight.

Comportement : Le casque coupe l'IA de vision (économie batterie/CPU). Il surveille le CO2 en priorité. Si le seuil est dépassé, il affiche une alerte rouge.

5. 🖥️ L'Interface Utilisateur (HUD)
L'affichage dans le casque n'est pas une simple vidéo. C'est une page Web (Flask) en temps réel.

A. Le HUD (Heads-Up Display)
Fond d'écran : Le flux vidéo caméra (faible latence).

Calque Widgets : Par-dessus la vidéo, des éléments HTML (divs) s'affichent ou se cachent selon les messages MQTT reçus.

Widget Vision : Dessine les cadres (Bounding Boxes) reçus du plugin Vision.

Widget Danger : Clignote en rouge si le plugin Gaz envoie une alerte.

Widget Système : Affiche CPU, Batterie, Heure.

B. Le Panneau de Contrôle (Web Interface)
Accessible via un navigateur externe (Smartphone/Tablette compagnon) ou via commandes vocales.

Permet de sélectionner le Profil.

Permet d'activer/désactiver un module manuellement ("Toggle").

Affiche l'état de santé du système (Logs).

6. 🛠️ Guide du Développeur : Comment étendre le système ?
Voici la procédure stricte pour ajouter des fonctionnalités sans casser le système existant.

Cas Pratique 1 : Ajouter un nouveau capteur (ex: Geiger/Radiation)
Hardware : Connecter le capteur au Arduino.

Code Arduino : Ajouter la lecture dans la boucle et l'envoyer sur le port Série (format JSON : {"rad": 120}).

Backbone (Pi) : Rien à faire ! Le Backbone lit tout le JSON de l'Arduino et le republie sur helmet/sensors/all.

Interface : Créer un petit widget HTML qui écoute helmet/sensors/all et affiche la valeur "rad".

Cas Pratique 2 : Ajouter une nouvelle IA (ex: Lecture de panneaux)
Modèle : Déposer ocr_traffic.pt dans le dossier /modeles.

Plugin : Créer le dossier /plugins/lecteur_panneaux.

Code Python (main.py) :

Se connecter au MQTT (localhost).

S'abonner à helmet/camera/raw.

Charger le modèle depuis ../../modeles/ocr_traffic.pt.

Traiter l'image.

Publier le texte lu sur helmet/plugins/lecteur_panneaux/text.

Activation : Ajouter "lecteur_panneaux" dans le fichier profiles.json sous le profil "Navigation".

7. 🚀 Résumé du Flux de Données (Data Flow)
Le Monde Réel -> Capteurs/Caméra.

Acquisition -> Arduino (Capteurs) / Libcamera (Vidéo).

Centralisation -> Backbone.py (Raspberry Pi).

Distribution -> MQTT Broker (Le Backbone publie tout).

Traitement -> Les Plugins (Vision, GPS...) écoutent MQTT, calculent, et republient les résultats.

Visualisation -> Le HUD (Navigateur Web dans le casque) écoute MQTT et met à jour l'affichage graphique par-dessus la vidéo.












1. 🏗️ Architecture Matérielle (Hardware)Le système est divisé en deux cerveaux : le Calcul (Haut Niveau) et le Sensoriel (Bas Niveau).A. Le Diagramme de ConnexionPlaintext       [ BATTERIE EXT (5V/3A) ]
                  |
        +---------+---------+
        |                   |
  [ RASPBERRY PI 5 ] <---> [ ARDUINO NANO/UNO ] (via USB)
  (Cerveau Principal)      (Cerveau Sensoriel)
        |                           |
        +-- [ CAMÉRA CSI ]          +-- [ Capteur Distance (HC-SR04) ]
        |                           |
        +-- [ ÉCRAN HUD (HDMI) ]    +-- [ Capteur Gaz (MQ-2) ]
        |                           |
        +-- [ CASQUE AUDIO ]        +-- [ Température (DHT22) ]
                                    |
                                    +-- [ GPS Module (NEO-6M) ]
B. Rôles MatérielsRaspberry Pi (Master) : Gère l'OS, le réseau (Wi-Fi/MQTT), l'affichage vidéo, et les calculs d'Intelligence Artificielle (YOLO).Arduino (Slave) : Gère l'acquisition de données brutes. Il nettoie les signaux des capteurs et envoie un paquet JSON propre à la Pi chaque 100ms.2. 💻 Architecture Logicielle (Software Stack)Le système repose sur une architecture Micro-Services asynchrone.CoucheTechnologieRôleInterface (UI)HTML5 / JS / SocketIOAffichage tête haute (HUD) et ContrôleCommunicationMQTT (Mosquitto)Bus de données universel (Le "Nerf" du système)OrchestrationPython (Backbone.py)Gestion des processus et des ProfilsIntelligencePython (Plugins)Modules indépendants (Vision, Nav, Danger)SystèmeLinux (Debian Bookworm)Gestion drivers Caméra (Libcamera) & USB3. 📂 Arborescence du Projet (File Structure)Voici comment organiser tes dossiers pour que le système soit propre et modulaire.PlaintextSHOS_Project/
│
├── backbone.py           # LE MAÎTRE : Lance les profils, gère le hardware, publie sur MQTT
├── profiles.json         # CONFIG : Définit quels plugins lancer pour "Mine", "Ville", etc.
├── requirements.txt      # DÉPENDANCES : Liste des librairies (flask, paho-mqtt, ultralytics...)
│
├── modeles/              # CERVEAUX IA (Stockage centralisé)
│   ├── yolov8n.pt        # Modèle détection objets standard
│   ├── gaz_risk.tflite   # Modèle prédiction danger gaz
│   └── ocr_text.pt       # Modèle lecture de texte
│
├── plugins/              # LES OUVRIERS (Un dossier = Une fonctionnalité)
│   ├── vision_objet/
│   │   ├── main.py       # Code du plugin (S'abonne à Camera, publie Detections)
│   │   └── config.json   # Paramètres spécifiques (ex: seuil de confiance)
│   │
│   ├── navigation_gps/
│   │   ├── main.py
│   │   └── maps_cache/   # Dossier local pour cartes hors-ligne
│   │
│   └── danger_monitor/   # (Surveillance Gaz/Température)
│       └── main.py
│
└── interface/            # LE VISAGE (Serveur Web Flask)
    ├── app.py            # Serveur Web léger
    ├── templates/
    │   └── hud.html      # La page vue dans les lunettes
    └── static/
        ├── style.css
        └── script.js     # Connecte le HUD au MQTT via Websocket
4. 🔄 Diagramme de Flux de Données (Data Flow)C'est le chemin que parcourt une information dans ton système.Étape 1 : Acquisition (INPUT)Caméra : Capture une image brute (Raw Bytes).Arduino : Lit Temp: 24°C, Gaz: 120ppm.Backbone : Récupère ces deux flux.Étape 2 : Distribution (BUS MQTT)Le Backbone ne traite rien. Il crie les infos sur le réseau :Publie sur helmet/camera/stream (L'image).Publie sur helmet/sensors/raw (Le JSON Arduino).Étape 3 : Traitement (PLUGINS)Les plugins actifs (selon le profil) écoutent :Plugin Vision attrape l'image -> Détecte "Personne" -> Publie {"box": [x,y,w,h], "label": "Personne"} sur helmet/vision/out.Plugin Danger attrape le JSON Arduino -> Analyse le gaz -> Si > 200, publie {"alert": "DANGER"} sur helmet/alert.Étape 4 : Visualisation (OUTPUT)Le HUD (Page Web) écoute tous les canaux de sortie (/vision/out, /alert, /sensors).Il dessine le cadre rouge sur la vidéo.Il fait clignoter l'écran si alerte gaz.5. ⚙️ Le Mécanisme de Profils (Orchestrateur)C'est la logique qui rend le système "Intelligent" et économe en énergie.Fichier profiles.json :JSON{
  "exploration_mine": {
    "description": "Priorité sécurité et environnement",
    "active_plugins": ["danger_monitor", "flashlight_control", "remote_assist"],
    "camera_fps": 15,
    "ai_model": "none"  // Pas d'IA vision pour économiser la batterie
  },
  "navigation_ville": {
    "description": "Assistance visuelle complète",
    "active_plugins": ["vision_objet", "ocr_lecture", "gps_guide"],
    "camera_fps": 30,
    "ai_model": "yolov8n.pt"
  }
}
Fonctionnement :Au démarrage, le système charge un profil par défaut.L'utilisateur dit "Mode Mine" (ou clique sur un bouton).L'Orchestrateur (Backbone) :TUE les processus vision_objet et ocr_lecture (Libération RAM).LANCE les processus danger_monitor.Change la configuration de la caméra.6. 🛡️ Sécurité et Robustesse (Watchdog)Pour un projet industriel, le système ne doit jamais planter totalement.Isolation des Processus : Chaque plugin tourne dans son propre coin. Si le plugin Vision crashe (erreur mémoire), le Backbone le voit, le tue, et le redémarre, SANS couper la vidéo ni les capteurs de gaz.Mode "Safe" : Si la batterie descend sous 15%, le Backbone force le profil "Économie" (Coupe toutes les IA, garde juste les capteurs vitaux).Logs : Tout est enregistré dans un fichier system.log pour comprendre les pannes après coup.
























non non non ! c'est pas ca la logique ! celui qui donneras l'ordre d'activer les modules c'est le script du profil utilisateur ! les mmodules et les profils sont gerer par le fichier de congiguration ! lui il atribue des modules a un profil ! la configuration as acces a tout les moduules et il les atribue au profil lors de ca création par le profil manager !   pour mieu expliquer, l'utilisateur cré son profil grace au profil manager ! le profil manager dit  a la configuraion  le profil qui as etait demander et tout les modules qui seront atribuer au profil !   puis la configuration crée le profil avec chacun des modules et capteur dont il a besoin ! puis il le met a la disposition de l'utilisateur sur son interface apreprier pour lui !  et si l'utilisateur crée un autre profil ! tout se fait pareil ! alors sur l'interface utilisateur au depart il n'y as qu'une pages d'aceil ! en suite quand il as créer des profiles, ils aparaissent sur sont interface et il peut en lancer un a un ! et quand il lance un profil, le module pricipale du profil s'active, et le reste peut etre activer ou des activer a partir de l'interface du profil ! tu as des questions ?

}