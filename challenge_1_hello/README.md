# Challenge 1 : Node Hello ROS2

## Description
Ce premier challenge consiste à créer un package ROS 2 en Python contenant un nœud simple. Ce nœud doit afficher le message **"Hello ROS2"** dans le terminal de manière répétitive toutes les **2 secondes**.

## Objectifs pédagogiques
* Création d'un workspace et d'un package ROS 2.
* Utilisation de la bibliothèque `rclpy`.
* Mise en place d'un **Timer** pour gérer la périodicité.
* Configuration des points d'entrée (`entry_points`) dans le fichier `setup.py`.

## Structure du code
* **Node Name** : `hello_node`
* **Timer Period** : 2.0 seconds
* **Logger** : `self.get_logger().info()`

## Installation et Exécution
1. **Compiler le package :**
   ```bash
   cd ~/challenge_ws
   colcon build --packages-select challenge_1_hello
2. **Sourcer l'environnement :**
   ```Bash
   source install/setup.bash

3. **Lancer le nœud :**
   ```Bash
   ros2 run challenge_1_hello hello_exe
