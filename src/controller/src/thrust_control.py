#!/usr/bin/env python
'''thrust_control ROS Node'''
import rospy
from std_msgs.msg import Float64
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)  #根据实际连接接口确定
eve=GPIO.PWM(40,50)      #输出频率
eve.start(2.5)           #初始转速


def callback(data):
    '''thrust_control Callback Function'''
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    try:
        while Ture:
            eve.ChangeDutyCycle(data.data)

    except:
        pass
    eve.stop()
    GPIO.cleanup

def listener():
    '''thrust_control Subscriber'''
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('thrust_control', anonymous=True)

    rospy.Subscriber("pwm_signal", Float64, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
