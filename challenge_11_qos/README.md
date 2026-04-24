# Challenge 11 : Gestion de la Qualité de Service (QoS)

## Objectif
L'objectif de ce challenge est de configurer des profils QoS spécifiques pour adapter la communication ROS 2 aux besoins réels du matériel (capteurs vs commandes).

## Profils Implémentés

### 1. Subscriber LiDAR (/scan)
- **Profil** : `Best Effort`
- **Justification** : Pour un capteur à haute fréquence comme le LiDAR, il est préférable de perdre quelques paquets de données plutôt que de retarder le flux complet. On privilégie la vitesse et la donnée la plus récente.
- **Paramètres** : `Reliability: BEST_EFFORT`, `Depth: 1`.

### 2. Publisher de Commandes (/critical_cmd)
- **Profil** : `Reliable`
- **Justification** : Pour des commandes critiques (comme un arrêt d'urgence), chaque message est vital. Le système doit garantir la réception du message par tous les abonnés.
- **Paramètres** : `Reliability: RELIABLE`, `Durability: TRANSIENT_LOCAL`.

## Instructions d'Exécution

### Compilation
```bash
cd ~/challenge_ws
colcon build --packages-select challenge_11_qos
source install/setup.bash
Lancement
Bash

ros2 run challenge_11_qos qos_exe

Vérification des QoS

Pendant que le nœud tourne, vous pouvez vérifier les paramètres appliqués avec :
Bash

ros2 topic info /scan --verbose
