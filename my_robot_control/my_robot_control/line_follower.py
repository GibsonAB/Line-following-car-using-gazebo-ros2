import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import cv2
import numpy as np

class LineFollower(Node):
    def __init__(self):
        super().__init__('line_follower')

        self.sub = self.create_subscription(
            Image, '/camera/image_raw', self.image_cb, 10)
        self.pub = self.create_publisher(
            Twist, '/cmd_vel', 10)

        self.bridge = CvBridge()

        self.v = 0.5          # forward speed (m/s)
        self.b = 0.3
        self.kp = 0.004       # steering gain

    def image_cb(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        self.get_logger().info("IMAGE RECEIVED")


        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, bw = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

        h, w = bw.shape
        roi = bw[int(0.7*h):h, :]   # bottom 30%

        M = cv2.moments(roi)
        if M['m00'] == 0:
            cmd = Twist()
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0
            self.pub.publish(cmd)
            return  # line lost

        cx = int(M['m10'] / M['m00'])
        error = cx - w//2
        cmd = Twist()
        cmd.linear.x = self.v - (self.v - self.b) * min(abs(error)/50.0, 1.0)
        cmd.angular.z = -self.kp * error
        self.pub.publish(cmd)
    

def main():
    rclpy.init()
    rclpy.spin(LineFollower())
    rclpy.shutdown()
