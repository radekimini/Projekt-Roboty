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

  def main(args=None):
    rclpy.init(args=args)
    node = OdomLogger()
    rclpy.spin(node)
    rclpy.shutdown()
