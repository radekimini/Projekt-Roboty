import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class CameraSubscriber(Node):
    def __init__(self, point_callback):
        super().__init__('camera_subscriber')
        self.subscription = self.create_subscription(
            Image,
            'image_raw',
            self.listener_callback,
            10
        )
        self.bridge = CvBridge()
        self.point_callback = point_callback
        self.window_name = "camera"

    def listener_callback(self, image_msg):
        frame = self.bridge.imgmsg_to_cv2(image_msg, "bgr8")
        cv2.imshow(self.window_name, frame)
        cv2.setMouseCallback(self.window_name, self.mouse_callback)
        cv2.waitKey(1)

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.point_callback(x, y)
