# Challenge 12 : Multi-threading et Callback Groups

## Description
Ce challenge démontre comment gérer l'exécution parallèle de tâches au sein d'un seul nœud ROS 2. L'objectif est d'empêcher qu'une tâche longue (Slow Callback) ne bloque les tâches prioritaires ou rapides (Fast Callback).

## Concepts Clés
1. **MultiThreadedExecutor** : Permet au nœud d'utiliser plusieurs threads pour traiter la file d'attente des callbacks.
2. **ReentrantCallbackGroup** : Une catégorie de groupe qui autorise l'exécution simultanée des callbacks qui lui sont rattachés.

## Structure du Code
- **Fast Callback** : S'exécute toutes les **50ms**.
- **Slow Callback** : S'exécute toutes les **500ms** et simule un calcul lourd avec `time.sleep(0.5)`.

## Comment tester ?
1. **Compiler le package** :
   ```bash
   cd ~/challenge_ws
   colcon build --packages-select challenge_12_threads
   source install/setup.bash
 
 Lancer le nœud :
    Bash

    ros2 run challenge_12_threads thread_exe

Observation attendue

Dans la console, vous remarquerez que les messages --- Callback RAPIDE s'affichent de manière fluide et régulière, même pendant que le message >>> DEBUT Callback LENT est affiché. Sans Multi-threading, le callback rapide aurait dû attendre la fin du callback lent pour s'afficher.
