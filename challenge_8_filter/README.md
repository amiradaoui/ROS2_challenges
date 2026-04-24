# Challenge 8 : Subscriber avec Filtre de Données

## Description
Ce challenge implémente un nœud qui surveille les données d'un capteur de température virtuel. Le nœud filtre les messages pour n'afficher des alertes que dans des conditions critiques.

## Logique de filtrage
Le nœud s'abonne au topic `/temperature` (type `Float64`) et utilise les seuils suivants :
- **Température > 30°C** : Affiche un message de type `WARN` (Alerte Élevée).
- **Température < 10°C** : Affiche un message de type `WARN` (Alerte Basse).
- **Entre 10°C et 30°C** : Affiche une simple information de type `INFO`.

## Comment tester
Publiez manuellement des valeurs sur le topic :
```bash
ros2 topic pub -1 /temperature std_msgs/msg/Float64 "{data: 35.0}"
