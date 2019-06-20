#!/usr/bin/env python
'''lmu ROS Node'''
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import serial
import sys

try:
    ser=serial.Serial('/dev/ttyACM0',9600)

except Exception, e:
    print 'open serial failed.'
    exit(1)

while True:
    s = ser.readline()
    am=str(s).strip().split(" ")
    if len(am)<14:
        continue
    else:
        a_x=am[2]
        a_y=am[4]
        a_z=am[6]
        m_x=am[9]
        m_y=am[11]
        m_z=am[13]

  





def talker():
    '''lmu Publisher'''
    pub = rospy.Publisher('/Course_real', Float64, queue_size=10)
    rospy.init_node('lmu', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(phi)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
