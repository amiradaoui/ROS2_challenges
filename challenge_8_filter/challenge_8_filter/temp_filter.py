import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class TempFilterNode(Node):
    def __init__(self):
        super().__init__('temp_filter_node')
        
        self.subscription = self.create_subscription(
            Float64,
            '/temperature',
            self.listener_callback,
            10)
        self.get_logger().info('Nœud de filtrage de température démarré...')

    def listener_callback(self, msg):
        temp = msg.data
        
        
        if temp > 30.0:
            self.get_logger().warn(f'ALERTE : Température trop ÉLEVÉE ! ({temp}°C)')
        elif temp < 10.0:
            self.get_logger().warn(f'ALERTE : Température trop BASSE ! ({temp}°C)')
        else:
           
            self.get_logger().info(f'Température normale : {temp}°C')

def main(args=None):
    rclpy.init(args=args)
    node = TempFilterNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
