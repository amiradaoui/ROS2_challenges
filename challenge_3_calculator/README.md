# Challenge 3 : Service Calculatrice

## Description
Ce challenge implémente un **Service ROS 2** nommé `/calcule`. Il utilise le modèle de communication synchrone (Requête/Réponse) pour effectuer des calculs entre deux nombres.

## Objectifs pédagogiques
* Compréhension du fonctionnement des services (Interfaces `.srv`).
* Utilisation de l'interface standard `example_interfaces/srv/AddTwoInts`.
* Mise en place d'un serveur de service capable de traiter des requêtes en temps réel.

## Instructions d'exécution

### 1. Compilation
```bash
cd ~/challenge_ws
colcon build --packages-select challenge_3_calculator
source install/setup.bash
### 2.Lancement du Serveur
```Bash
ros2 run challenge_3_calculator calculator_service_exe

3. Appel du Service (Client)

Dans un nouveau terminal, exécutez la commande suivante :
Bash

ros2 service call /calcule example_interfaces/srv/AddTwoInts "{a: 10, b: 5}"

Résultat obtenu

Le service renvoie la somme des deux nombres fournis dans la requête
