import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random # لاستخدام الضجيج العشوائي

class TempPublisher(Node):
    def __init__(self):
        super().__init__('temp_publisher_node')
        # إنشاء الناشر (Publisher) على موضوع اسمه /temperature
        self.publisher_ = self.create_publisher(Float64, 'temperature', 10)
        
        # إنشاء مؤقت يعمل بتردد 1 هرتز (مرة كل ثانية)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Temperature Publisher has started!')

    def timer_callback(self):
        msg = Float64()
        # حساب الحرارة: 20 درجة + قيمة عشوائية بين -1 و 1
        noise = random.uniform(-1.0, 1.0)
        msg.data = 20.0 + noise
        
        # نشر الرسالة
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing Temperature: {msg.data:.2f}°C')

def main(args=None):
    rclpy.init(args=args)
    node = TempPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
