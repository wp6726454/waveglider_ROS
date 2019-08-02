import pigpio
import time
pi = pigpio.pi()
pi.set_PWM_frequency(23,50)
pi.set_PWM_range(23,20000)
try:
	while 1:
		for dc in range(1500,1900,50):
			pi.set_PWM_dutycycle(23,dc)
			time.sleep(1)
		for dc in range(1900,1500,-50):
		    pi.set_PWM_dutycycle(23,dc)
		    time.sleep(1)
		for dc in range(1500,1100,-50):
			pi.set_PWM_dutycycle(23,dc)
			time.sleep(1)
		for dc in range(1100,1500,50):
			pi.set_PWM_dutycycle(23,dc)
			time.sleep(1)
except KeyboardInterrupt:
	pass
pi.stop()
