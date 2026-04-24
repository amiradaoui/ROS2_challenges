# Challenge 6 : Action Server Navigation (Simulation)

## Description
Ce challenge implémente un **Action Server** qui simule le déplacement d'un robot vers une cible. Contrairement aux services, l'action fournit un **feedback** en temps réel sur la distance restante.

## Fonctionnement
- **Goal** : L'utilisateur envoie une commande de navigation.
- **Feedback** : Le serveur publie chaque seconde la distance restante (5m, 4m, 3m...).
- **Result** : Une fois arrivé à 0m, l'action se termine avec succès.

## Commande pour tester
```bash
ros2 action send_goal /navigate example_interfaces/action/Fibonacci "{order: 5}" --feedback
