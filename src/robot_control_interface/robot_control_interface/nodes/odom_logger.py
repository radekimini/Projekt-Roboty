import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class OdomLogger(Node):
    def __init__(self):
        super().__init__('odom_logger_node')

        self.last_x = None
        self.last_y = None

        self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        self.get_logger().info('Odom logger node started')
        
        def odom_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        if self.last_x is None or self.last_y is None:
            self.last_x = x
            self.last_y = y
            return

        if x != self.last_x or y != self.last_y:
            self.get_logger().info(f'Robot position changed: x={x:.3f}, y={y:.3f}')
            self.last_x = x
            self.last_y = y

  def main(args=None):
    rclpy.init(args=args)
    node = OdomLogger()
    rclpy.spin(node)
    rclpy.shutdown()
