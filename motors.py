import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(7.5)

m = GPIO.PWM(11,50)
m.start(7.5)

try:
	while True:
		p.ChangeDutyCycle(7.5)
		m.ChangeDutyCycle(7.5)
		time.sleep(1)
		p.ChangeDutyCycle(12.5)
		m.ChangeDutyCycle(12.5)
		time.sleep(1)
		p.ChangeDutyCycle(2.5)
		m.ChangeDutyCycle(2.5)
		time.sleep(1)
		
except KeyboardInterrupt:
	p.stop()
	m.stop()
	GPIO.cleanup()
