#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import cv2
import numpy as np
import time


class ClickControlNode(Node):
    def __init__(self):
        super().__init__('click_control_node')


        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        self.window_height = 512
        self.window_width = 512
        self.window_name = "Robot control"

        self.image = np.zeros((self.window_height, self.window_width, 3), dtype=np.uint8)

        self.current_speed = 0.0
        self.command_until = 0.0

        cv2.namedWindow(self.window_name)
        cv2.setMouseCallback(self.window_name, self.mouse_callback)

        self.get_logger().info("Click control node started")

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.current_speed = 0.2 if y < self.window_height / 2 else -0.2
            self.command_until = time.time() + 0.5
            self.get_logger().info(f"Click -> speed {self.current_speed}")

    def update(self):
        self.image[:] = 0
        center_y = self.window_height // 2
        cv2.line(self.image, (0, center_y), (self.window_width, center_y), (255, 255, 255), 1)
        cv2.imshow(self.window_name, self.image)
        cv2.waitKey(1)

        if time.time() < self.command_until:
            msg = Twist()
            msg.linear.x = self.current_speed
            self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = ClickControlNode()

    try:
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec=0.01)
            node.update()
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
