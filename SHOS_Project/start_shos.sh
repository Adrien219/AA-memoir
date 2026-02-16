#!/bin/bash

# Chemin du projet
PROJECT_ROOT="/home/jmk/memoir/AA-memoir/SHOS_Project"

echo "--- DÉMARRAGE DU SYSTÈME S.H.O.S ---"

# 1. S'assurer que le Broker MQTT tourne
echo "[1/4] Vérification de Mosquitto..."
sudo systemctl start mosquitto

# 2. Lancer le Backbone (IA) en arrière-plan
echo "[2/4] Lancement du Backbone (IA)..."
cd $PROJECT_ROOT
python3 backbone.py & 
PID_BACKBONE=$!

# Attendre que le modèle YOLO charge (environ 5-10 sec selon le Pi)
sleep 8

# 3. Lancer le Bridge (Pont MQTT)
echo "[3/4] Lancement du Bridge..."
python3 bridge.py &
PID_BRIDGE=$!

sleep 2

# 4. Lancer l'Interface (Serveur Flask)
echo "[4/4] Lancement de l'Interface HUD..."
cd interface
python3 app.py &
PID_APP=$!

echo "------------------------------------"
echo "SYSTÈME ACTIF !"
echo "HUD disponible sur http://localhost:5000"
echo "Appuyez sur [CTRL+C] pour tout arrêter."
echo "------------------------------------"

# Fonction pour tout arrêter proprement à la fermeture
trap "kill $PID_BACKBONE $PID_BRIDGE $PID_APP; echo 'Système arrêté.'; exit" INT

# Garde le script ouvert pour voir les logs
wait
