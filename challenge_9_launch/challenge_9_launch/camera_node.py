import rclpy
from rclpy.node import Node

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        # Déclaration des paramètres avec leurs valeurs par défaut
        self.declare_parameter('resolution', '720p')
        self.declare_parameter('fps', 30)

        # Récupération des valeurs
        res = self.get_parameter('resolution').get_parameter_value().string_value
        fps = self.get_parameter('fps').get_parameter_value().integer_value

        self.get_logger().info(f'Caméra démarrée en {res} à {fps} FPS')

def main(args=None):
    rclpy.init(args=args)
    node = CameraNode()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
