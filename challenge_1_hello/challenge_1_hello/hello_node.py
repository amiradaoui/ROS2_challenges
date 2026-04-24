import rclpy
from rclpy.node import Node

class HelloNode(Node):
    def __init__(self):
        super().__init__('hello_node')
       
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.get_logger().info('تم تشغيل العقدة بنجاح!')

    def timer_callback(self):
       
        self.get_logger().info('Hello ROS2')

def main(args=None):
    rclpy.init(args=args)
    node = HelloNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
