import rclpy
from robot_control_interface.nodes.velocity_publisher import VelocityPublisher
from robot_control_interface.logic.velocity_logic import VelocityLogic
from robot_control_interface.logic.point_analyzer import PointAnalyzer
from robot_control_interface.utils.constants import WINDOW_HEIGHT


class ControllerNode:
    def __init__(self):
        self.analyzer = PointAnalyzer(WINDOW_HEIGHT)
        self.velocity_logic = VelocityLogic()
        self.publisher = VelocityPublisher()

    def process_point(self, point):
        if point is None:
            return

        _, y = point

        if self.analyzer.is_point_above_center(y):
            msg = self.velocity_logic.forward()
        else:
            msg = self.velocity_logic.stop()

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    controller = ControllerNode()
    rclpy.spin(controller.publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
