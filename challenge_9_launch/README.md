# Challenge 9 : Automation avec Launch Files et Arguments

## Description
Ce challenge démontre l'utilisation des fichiers de lancement (**Launch Files**) en Python pour automatiser le démarrage des nœuds ROS 2. L'objectif est de pouvoir configurer un nœud au moment du lancement sans modifier son code source, en utilisant des arguments de ligne de commande.

## Fonctionnalités
Le nœud `camera_node` simule le démarrage d'une caméra et accepte deux paramètres configurables :
1.  **resolution** : La définition de l'image (ex: 720p, 1080p, 4K).
2.  **fps** : Le nombre d'images par seconde (Frames Per Second).

## Structure du Launch File
Le fichier `simulation_launch.py` effectue les actions suivantes :
- Déclaration des arguments via `DeclareLaunchArgument`.
- Récupération des valeurs via `LaunchConfiguration`.
- Passage des valeurs au nœud sous forme de paramètres ROS 2.

## Instructions d'Exécution

### 1. Compilation
```bash
cd ~/challenge_ws
colcon build --packages-select challenge_9_launch
source install/setup.bash
````
2. Lancement avec les valeurs par défaut, la caméra se lance en 720p à 30 FPS :
````Bash
ros2 launch challenge_9_launch simulation_launch.py
````
3. Lancement avec arguments personnalisés Pour modifier la configuration (par exemple 1080p et 60 FPS) :
````Bash
ros2 launch challenge_9_launch simulation_launch.py resolution:='1080p' fps:=60
````
Résultat Attendu

Le nœud affiche dans la console un message de confirmation indiquant les paramètres reçus :
[INFO] [camera_node]: Caméra démarrée en 1080p à 60 FPS
