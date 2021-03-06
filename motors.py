import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

m = GPIO.PWM(11,50)
m.start(7)

p = GPIO.PWM(7,50)
p.start(6)

try:
	while True:
		key = raw_input("direction: ")
		if key == 'q':
			print("Going forward!")
			m.ChangeDutyCycle(12.5)
			#time.sleep(1)
			print("Done!")
		if key == "a":
			print("Stationary!")
			m.ChangeDutyCycle(7)
			#time.sleep(1)
			print("Done!")
		if key == "z":
			print("Going backward!")
			m.ChangeDutyCycle(1.5)
			#time.sleep(1)
			print("Done!")

		if key == "w":
			print("Going left!")
			p.ChangeDutyCycle(10)
			#time.sleep(1)
			print("Done!")
		if key == "s":
			print("Stationary!")
			p.ChangeDutyCycle(6)
			#time.sleep(1)
			print("Done!")
		if key == "x":
			print("Stationary!")
			p.ChangeDutyCycle(1.5)
			#time.sleep(1)
			print("Done!")
except KeyboardInterrupt:
	p.stop()
	m.stop()
	GPIO.cleanup()
