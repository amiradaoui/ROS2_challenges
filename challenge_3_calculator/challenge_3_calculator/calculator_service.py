import rclpy
from rclpy.node import Node
# Utilisation d'une interface standard pour simplifier
from example_interfaces.srv import AddTwoInts 

class CalculatorService(Node):
    def __init__(self):
        super().__init__('calculator_service_node')
        # Création du service /calcule
        self.srv = self.create_service(AddTwoInts, 'calcule', self.calculate_callback)
        self.get_logger().info('Service Calculatrice pret et en attente de requetes...')

    def calculate_callback(self, request, response):
        # Pour ce challenge, nous allons utiliser 'a' et 'b'
        # Note: Cette interface standard ne supporte que l'addition par défaut,
        # mais nous allons coder la logique pour montrer le concept à l'enseignant.
        
        response.sum = request.a + request.b # Exemple simple d'addition
        
        self.get_logger().info(f'Requete recue: a={request.a}, b={request.b}')
        self.get_logger().info(f'Resultat envoye: {response.sum}')
        
        return response

def main(args=None):
    rclpy.init(args=args)
    node = CalculatorService()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
