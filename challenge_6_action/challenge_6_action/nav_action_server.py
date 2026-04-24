import rclpy
import time
import math
from rclpy.action import ActionServer
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped

from example_interfaces.action import Fibonacci 

class NavActionServer(Node):
    def __init__(self):
        super().__init__('nav_action_server')
        self._action_server = ActionServer(
            self,
           
           
            Fibonacci,
            'navigate',
            self.execute_callback)
        self.get_logger().info('Action Server Navigation démarré...')

    def execute_callback(self, goal_handle):
        self.get_logger().info('Exécution de la navigation...')
        feedback_msg = Fibonacci.Feedback()
        
        #  (Distance restante)
        for i in range(1, 6):
            distance_restante = 5.0 - float(i)
            # feedback
            feedback_msg.sequence = [int(distance_restante)] 
            self.get_logger().info(f'Feedback: Distance restante = {distance_restante}m')
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1.0) 

        goal_handle.succeed()
        result = Fibonacci.Result()
        result.sequence = [0] 
        self.get_logger().info('Cible atteinte avec succès !')
        return result

def main(args=None):
    rclpy.init(args=args)
    node = NavActionServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
