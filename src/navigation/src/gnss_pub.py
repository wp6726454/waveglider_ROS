#!/usr/bin/env python
'''BD ROS Node'''
# license removed for brevity
import rospy
from std_msgs.msg import UInt64MultiArray
import serial
#from lmu_pub import datafilter
#import numpy as np
#from math import sin, cos, atan

def talker():
    '''lmu Publisher'''
    pub = rospy.Publisher('/position_real', UInt64MultiArray, queue_size=10)
    rospy.init_node('gnss', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    try:
        ser=serial.Serial('/dev/ttyUSB0',9600)

    except Exception:
        print 'open serial failed.'
        exit(1)

    while True:
        s = ser.readline()
        am=str(s).strip().split(" ")
        if len(am)<30:
            continue
        else:
            lon=float(am[11])
            lat=float(am[12])


            while not rospy.is_shutdown():
                pos = [lon, lat]
                pub.publish(pos)
                rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
