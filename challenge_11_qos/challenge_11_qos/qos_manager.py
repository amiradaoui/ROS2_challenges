import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

class QoSNode(Node):
    def __init__(self):
        super().__init__('qos_manager_node')

       
        lidar_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            history=HistoryPolicy.KEEP_LAST,
            depth=1, # نريد آخر مسح فقط
            durability=DurabilityPolicy.VOLATILE
        )

       
        cmd_qos = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            history=HistoryPolicy.KEEP_LAST,
            depth=10, # تخزين الأوامر لضمان وصولها
            durability=DurabilityPolicy.TRANSIENT_LOCAL
        )

        
        self.sub = self.create_subscription(
            LaserScan, '/scan', self.lidar_callback, lidar_qos)

        
        self.pub = self.create_publisher(
            String, '/critical_cmd', cmd_qos)

        self.get_logger().info("Nœud QoS configuré et prêt.")

    def lidar_callback(self, msg):
        
        self.get_logger().info("Données LiDAR reçues (Best Effort)")

    def send_command(self, text):
        msg = String()
        msg.data = text
        self.pub.publish(msg)
        self.get_logger().warn(f"Commande CRITIQUE envoyée : {text} (Reliable)")

def main(args=None):
    rclpy.init(args=args)
    node = QoSNode()
    node.send_command("STOP_ROBOT") 
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
