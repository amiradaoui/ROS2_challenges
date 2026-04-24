import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StatusPub(Node):
    def __init__(self):
        super().__init__('status_node')
        # Correction BUG 1 : Ajout du '/' pour un nom de topic global
        self.pub = self.create_publisher(String, '/robot/status', 10)
        # Création du timer (1 seconde)
        self.timer = self.create_timer(1.0, self.cb)
        self.get_logger().info("Le nœud de débogage a démarré correctement.")

    def cb(self):
        # Correction BUG 2 : Instanciation correcte de l'objet String()
        msg = String()
        msg.data = 'OK'
        # Correction BUG 3 : Passage de l'argument 'msg' à la fonction publish
        self.pub.publish(msg)
        self.get_logger().info('Publication : OK')

def main(args=None):
    rclpy.init(args=args)
    node = StatusPub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
