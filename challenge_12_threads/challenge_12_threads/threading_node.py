import rclpy
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
import time

class ParallelNode(Node):
    def __init__(self):
        super().__init__('parallel_executor_node')
        
        
        self.group = ReentrantCallbackGroup()

        
        self.fast_timer = self.create_timer(
            0.05, self.fast_callback, callback_group=self.group)

      
        self.slow_timer = self.create_timer(
            0.5, self.slow_callback, callback_group=self.group)

        self.get_logger().info("Node MultiThreaded prêt.")

    def fast_callback(self):
        self.get_logger().info('--- Callback RAPIDE (50ms)')

    def slow_callback(self):
        self.get_logger().warn('>>> DEBUT Callback LENT (500ms)')
        time.sleep(0.5) # محاكاة عملية ثقيلة
        self.get_logger().warn('<<< FIN Callback LENT')

def main(args=None):
    rclpy.init(args=args)
    node = ParallelNode()

   
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
