from geometry_msgs.msg import Twist
from robot_control_interface.utils.constants import LINEAR_SPEED, STOP_SPEED

class VelocityLogic:
    def forward(self):
        msg = Twist()
        msg.linear.x = LINEAR_SPEED
        return msg

    def stop(self):
        msg = Twist()
        msg.linear.x = STOP_SPEED
        return msg
