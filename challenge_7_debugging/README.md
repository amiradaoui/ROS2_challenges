# Challenge 7 : Débogage d'un Publisher Silencieux

## Description
Ce challenge consistait à diagnostiquer et corriger un nœud ROS 2 (Python) qui ne parvenait pas à publier des données sur le topic `/robot/status`. Trois erreurs majeures (Bugs) empêchaient le bon fonctionnement du code original.

## Analyse des Erreurs et Corrections

### Bug 1 : Nom du Topic (Namespace)
- **Erreur :** Le nom du topic était défini comme `'robot/status'`.
- **Correction :** Ajout d'un slash initial : `'/robot/status'`.
- **Pourquoi :** En ROS 2, il est préférable d'utiliser des chemins absolus (avec `/`) pour s'assurer que le topic est accessible globalement, surtout lorsqu'on travaille avec plusieurs namespaces.

### Bug 2 : Instanciation du Message
- **Erreur :** `msg = String`
- **Correction :** `msg = String()`
- **Pourquoi :** `String` est la classe (le type) du message. Pour créer un objet message réel que l'on peut remplir de données, il faut instancier la classe en utilisant des parenthèses.

### Bug 3 : Méthode de Publication
- **Erreur :** `self.pub.publish()`
- **Correction :** `self.pub.publish(msg)`
- **Pourquoi :** La méthode `publish` a besoin de savoir *quoi* publier. Il faut lui passer l'objet `msg` contenant les données en argument.

## Instructions d'Exécution
1. **Compilation :**
   ```bash
   cd ~/challenge_ws
   colcon build --packages-select challenge_7_debugging
   source install/setup.bash
2. **Lancement du nœud :**
   ```bash
    ros2 run challenge_7_debugging status_pub_exe
 
 Résultat Attendu

Le terminal affichera le message data: "OK" de manière continue chaque seconde.
