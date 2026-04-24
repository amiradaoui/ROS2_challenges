# Challenge 10 : Client d'Action Asynchrone (Non-bloquant)

## Problème Identifié
Le client d'action original utilisait un appel synchrone qui bloquait l'exécution du thread principal. Cela empêchait le nœud de traiter d'autres événements ou messages tant que l'action n'était pas terminée.

## Solution : Programmation Asynchrone
Dans cette version corrigée :
1. J'ai remplacé `send_goal()` par **`send_goal_async()`**.
2. J'ai utilisé des **Futures** et des **Callbacks** (`add_done_callback`).
3. Cela permet au nœud de rester "vivant" (spin) et de continuer à répondre au système pendant que le serveur d'action traite la navigation.

## Commande de lancement
```bash
ros2 run challenge_10_async async_client_exe
