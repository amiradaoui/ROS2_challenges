import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose

class NavClient(Node):
    def __init__(self):
        super().__init__('nav_client_async')
        self._client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self.get_logger().info("Client d'action prêt (Non-bloquant).")

    def send_goal_to(self, x, y):
       
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.pose.position.x = float(x)
        goal_msg.pose.pose.position.y = float(y)
        goal_msg.pose.header.frame_id = 'map'

        
        self._client.wait_for_server()

        
        self.get_logger().info(f"Envoi de l'objectif (x={x}, y={y})...")
        self._send_goal_future = self._client.send_goal_async(goal_msg)
        
        
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().warn('Objectif refusé par le serveur.')
            return

        self.get_logger().info('Objectif accepté ! Le robot est en route.')
        
        
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Mission terminée avec succès !')

def main(args=None):
    rclpy.init(args=args)
    node = NavClient()
   
    node.send_goal_to(2.0, 3.5)
    rclpy.spin(node)
    rclpy.shutdown()
