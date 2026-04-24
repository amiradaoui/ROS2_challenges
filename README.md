# 🤖 ROS 2 Jazzy : Portfolio des 12 Challenges

Ce dépôt regroupe l'ensemble de mes travaux pratiques réalisés sur ROS 2 Jazzy (Ubuntu 24.04). Chaque dossier contient un package spécifique répondant à un défi technique du cursus.

## 🚀 Liste des Challenges

| # | Nom du Challenge | Concepts Clés |
|---|------------------|---------------|
| 01 | Hello World | Création et exécution de nœuds Python simples. |
| 02 | Temp Publisher | Utilisation des Topics et messages standards (String, Float64). |
| 03 | Calculator Service| Communication Client/Serveur via les Services ROS 2. |
| 04 | TF2 Broadcaster | Gestion des transformations de coordonnées (Frames). |
| 05 | Lifecycle Nodes | Gestion déterministe des états d'un nœud (Configure, Activate). |
| 06 | Nav Action | Implémentation de serveurs d'Actions (Goal, Feedback, Result). |
| 07 | Debugging | Utilisation des logs (get_logger) et outils d'introspection. |
| 08 | Filter Node | Traitement et filtrage de données en temps réel. |
| 09 | Launch Files | Automatisation du démarrage de plusieurs nœuds simultanément. |
| 10 | Async Client | Appels de services non-bloquants (Asynchronous calls). |
| 11 | QoS Config | Paramétrage de la Qualité de Service (Reliability & Durability). |
| 12 | Multi-threading | Utilisation de MultiThreadedExecutor et CallbackGroups. |

## 🛠️ Installation & Utilisation

### Prérequis
- ROS 2 Jazzy installé sur Ubuntu 24.04.
- Workspace configuré (ex: ~/challenge_ws).

### Compilation
`bash
cd ~/challenge_ws
colcon build
source install/setup.bash
