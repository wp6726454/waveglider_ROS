#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import pynmea2
import time
import rospy
from message.msg import GNSS_msg
from std_msgs.msg import String
def callback(GNSS_msg):
	rospy.loginfo('listener:经度=%f ,纬度= %f',lat,lon)
def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber('gnss_info', GNSS_msg, callback)
	rospy.spin()
if __name__ == '__main__':
listener()