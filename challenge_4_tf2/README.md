# Challenge 4 : TF2 Broadcaster Dynamique

## Description
Ce challenge consiste à diffuser une transformation (TF) dynamique entre le repère `world` (parent) et le repère `robot` (enfant). Le robot effectue une rotation continue sur l'axe **Z** avec une vitesse angulaire de **0.5 rad/s**.

## Concepts clés
* Utilisation de `tf2_ros.TransformBroadcaster`.
* Manipulation des messages `geometry_msgs/TransformStamped`.
* Conversion d'un angle d'Euler (Yaw) en **Quaternions**.

## Comment visualiser
1. Lancer le broadcaster :
   `ros2 run challenge_4_tf2 tf_broadcaster_exe`
2. Ouvrir RViz2 :
   `rviz2`
3. Configurer le "Fixed Frame" sur `world` et ajouter le module `TF`.
