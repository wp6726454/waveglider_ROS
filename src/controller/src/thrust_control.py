#!/usr/bin/env python
'''thrust_control ROS Node'''
import rospy
from std_msgs.msg import Float64
import pigpio
from PID import PID
import json

class PID_controllor():

    def __init__(self):
        rospy.init_node('pwmbuilder', anonymous=True)
        rate = rospy.Rate(1) # 1hz
        self.course_real = 0.0
        self.course_desired = 0.0
        rospy.Subscriber("/course_real", Float64, self.callback_real)
        rospy.Subscriber("/course_desired", Float64, self.callback_desired)
        rate.sleep()
        controllor = PID(5, 6, 0.1, -10, 10, -0.5, 0.5)
        pi = pigpio.pi()
        pi.set_PWM_frequency(23,50)  
        pi.set_PWM_range(23,20000)
        while not rospy.is_shutdown():
            #calculate thrust by PID
            F = controllor.update(self.course_real, self.course_desired)
            #calculate pwm signal
            dc=-2.9*F

    	    dc_save='dc.json'
            with open(dc_save,'a') as dc_obj:
                dc_obj.write('\n'+str(dc))
            count = len(open(dc_save, 'r').readlines())
            if count < 200:
                pass
            else:
                for line in fileinput.input('dc.json', inplace=1):
                    if not fileinput.isfirstline():
                        print(line.replace('\n',''))
                for line in fileinput.input('dc.json', inplace=1):
                    if not fileinput.isfirstline():
                        print(line.replace('\n',''))


            with open(dc_save,'r') as f:
                lines=f.readlines()
                last_dc=lines[-1]
            if last_dc < dc:
                for i in range(last_dc,dc):
                    pi.set_PWM_dutucycle(23,i)
            elif last_dc > dc:
                for i in range(dc,last_dc):
                    pi.set_PWM_dutucycle(23,i)
                else:
                    pi.set_PWM_dutucycle(23,dc)       

            rospy.loginfo("the result is %f", dc)


    def callback_real(self, msg): 
        rospy.loginfo("the real course now is : %f", msg.data)
        self.course_real = msg.data
        
    def callback_desired(self, msg): 
        rospy.loginfo("the desired course now is : %f", msg.data)
        self.course_desired = msg.data

if __name__ == '__main__':
    try:
        PID_controllor()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    
