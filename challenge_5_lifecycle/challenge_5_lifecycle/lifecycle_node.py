import rclpy
from rclpy.lifecycle import LifecycleNode, State, TransitionCallbackReturn
from std_msgs.msg import String

class MyLifecycleNode(LifecycleNode):
    def __init__(self):
        # Initialisation du nœud avec le nom 'lc_node'
        super().__init__('lc_node')
        self.publisher_ = None
        self.timer_ = None

    def on_configure(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Configuration du nœud...")
        # Création du publisher (mais il ne publiera pas encore)
        self.publisher_ = self.create_lifecycle_publisher(String, 'lifecycle_topic', 10)
        self.timer_ = self.create_timer(1.0, self.publish_callback)
        return TransitionCallbackReturn.SUCCESS

    def on_activate(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Nœud ACTIVÉ : début de la publication.")
        # Le système active automatiquement le lifecycle_publisher ici
        return super().on_activate(state)

    def on_deactivate(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Nœud DÉSACTIVÉ : arrêt de la publication.")
        return super().on_deactivate(state)

    def on_cleanup(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Nettoyage (Cleanup) en cours...")
        self.destroy_timer(self.timer_)
        self.destroy_publisher(self.publisher_)
        return TransitionCallbackReturn.SUCCESS

    def publish_callback(self):
        msg = String()
        msg.data = "Données du nœud actif"
        # Le message ne sera réellement envoyé que si l'état est 'active'
        if self.publisher_ is not None:
            self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyLifecycleNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
