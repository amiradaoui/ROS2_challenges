# Challenge 2 : Publisher de Température

## Description
Simulation d'un capteur de température qui publie des données de type `Float64` sur le topic `/temperature` avec une fréquence de **1Hz**. La valeur publiée est de **20°C** avec un **bruit aléatoire** ajouté.

## Installation et Exécution
```bash
colcon build --packages-select challenge_2_temperature
source install/setup.bash
ros2 run challenge_2_temperature temp_pub_exe
