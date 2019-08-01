#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import pynmea2
import time
import rospy
from message.msg import GNSS_msg
ser = serial.Serial("/dev/ttyAMA0",9600)
try:
	while True:
	    line = ser.readline()
	    if line.startswith('$GNRMC'):
	        rmc = pynmea2.parse(line)
	        lat=float(rmc.lat)/100
	        lon=float(rmc.lon)/100
	        break
	    def talker():
	    	pub = rospy.Publisher('gnss_info', GNSS_msg , queue_size=10)
	        rospy.init_node('talker', anonymous=True)
	        rate = rospy.Rate(1)
	        while not rospy.is_shutdown():
				rospy.loginfo('Talker:经度=%f ,纬度= %f',lat,lon)
				pub.publish(GNSS_msg(lat,lon))
				rate.sleep()
		if __name__ == '__main__':
			talker()
except rospy.ROSInterruptException:
    pass