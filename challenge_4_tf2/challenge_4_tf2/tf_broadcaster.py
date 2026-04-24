import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
import math

class DynamicTFBroadcaster(Node):
    def __init__(self):
        super().__init__('tf_broadcaster_node')
        
        # Initialisation du diffuseur TF
        self.tf_broadcaster = TransformBroadcaster(self)
        
        # Timer pour mettre à jour la transformation (30Hz pour fluidité)
        self.timer = self.create_timer(0.033, self.broadcast_timer_callback)
        self.start_time = self.get_clock().now()
        
        self.get_logger().info('TF2 Broadcaster démarré : le robot tourne à 0.5 rad/s')

    def broadcast_timer_callback(self):
        t = TransformStamped()

        # Header
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'world'
        t.child_frame_id = 'robot'

        # Position (le robot reste au centre pour ce défi)
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0

        # Calcul de l'angle (0.5 rad/s)
        now = self.get_clock().now()
        elapsed_time = (now - self.start_time).nanoseconds / 1e9
        angle = 0.5 * elapsed_time

        # Conversion de l'angle (Yaw) en Quaternion (nécessaire pour TF2)
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = math.sin(angle / 2.0)
        t.transform.rotation.w = math.cos(angle / 2.0)

        # Envoi de la transformation
        self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = DynamicTFBroadcaster()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()

if __name__ == '__main__':
    main()
