# Challenge 5 : Lifecycle Node (Nœud à cycle de vie)

## Description
Ce challenge démontre la gestion avancée des ressources dans ROS 2 via un **Lifecycle Node**. Le nœud possède des états de transition (Unconfigured, Inactive, Active) qui permettent de contrôler l'exécution du code de manière déterministe.

## Logique Implémentée
- **on_configure** : Initialise le `LifecyclePublisher` et le `Timer`.
- **on_activate** : Active le flux de données sur le topic `/lifecycle_topic`.
- **on_deactivate** : Suspend la publication des messages.
- **on_cleanup** : Détruit les ressources pour libérer la mémoire.

## Procédure de Test (Essentiel)
Contrairement aux nœuds classiques, ce nœud doit être géré manuellement pour passer d'un état à l'autre.

1. **Lancer le nœud :**
   ```bash
   ros2 run challenge_5_lifecycle lc_node_exe
2. **Configurer le nœud :**
    ``Bash
    ros2 lifecycle set /lc_node configure

3. **Activer le nœud (Démarrage du flux) :**
    ```Bash
    ros2 lifecycle set /lc_node activate

4. **Vérifier les messages :**
    ```Bash
    ros2 topic echo /lifecycle_topic

Conclusion

Ce nœud prouve qu'il est possible de gérer finement le démarrage et l'arrêt des capteurs ou actuateurs d'un robot sans arrêter complètement le processus.
