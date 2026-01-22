import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


class UR5TrajectoryNode(Node):
    def __init__(self):
        super().__init__('ur5_node')

        self.publisher = self.create_publisher(
            JointTrajectory,
            '/joint_trajectory_controller/joint_trajectory',
            10
        )

        self.timer = self.create_timer(1.0, self.publish_trajectory)
        self.sent = False

        self.get_logger().info('UR5 joint trajectory publisher started')

    def publish_trajectory(self):
        if self.sent:
            return

        msg = JointTrajectory()
        # stamp = 0 jest wymagane przez joint_trajectory_controller
        msg.header.stamp.sec = 0
        msg.header.stamp.nanosec = 0
        msg.header.frame_id = 'base_link'

        msg.joint_names = [
            'shoulder_pan_joint',
            'shoulder_lift_joint',
            'elbow_joint',
            'wrist_1_joint',
            'wrist_2_joint',
            'wrist_3_joint'
        ]

        start = JointTrajectoryPoint()
        start.positions = [-1.57, 0.0, -1.57, 0.0, 0.0, 0.0]
        start.time_from_start.sec = 0

        goal = JointTrajectoryPoint()
        goal.positions = [0.0, -1.57, 1.57, 0.0, 0.0, 0.0]
        goal.time_from_start.sec = 5

        msg.points.append(start)
        msg.points.append(goal)

        self.publisher.publish(msg)
        self.sent = True

        self.get_logger().info('Joint trajectory published')


def main():
    rclpy.init()
    node = UR5TrajectoryNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
