import rclpy
from robot_control_interface.nodes.camera_subscriber import CameraSubscriber
from robot_control_interface.logic.point_analyzer import PointAnalyzer
from robot_control_interface.utils.constants import WINDOW_HEIGHT


class CameraNode:
    def __init__(self):
        self.analyzer = PointAnalyzer(WINDOW_HEIGHT)
        self.last_point = None

    def point_received(self, x, y):
        self.last_point = (x, y)

def main(args=None):
    rclpy.init(args=args)

    camera_logic = CameraNode()
    camera_node = CameraSubscriber(camera_logic.point_received)

    rclpy.spin(camera_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
