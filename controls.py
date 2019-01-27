import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT) # LEFT
GPIO.setup(11, GPIO.OUT) # RIGHT
GPIO.setup(13, GPIO.OUT) # FORWARD
GPIO.setup(15, GPIO.OUT) # BACKWARD

# initialize stopped car

GPIO.output(15, False)
GPIO.output(13, False)
GPIO.output(7, False)
GPIO.output(11, False)

while True:
	key = raw_input("direction: ")
	if key == 'q':
		print("Going forward!")
		GPIO.output(15, False)
		GPIO.output(13, True)
	if key == 'a':
		print("Stationary!")
		GPIO.output(13, False)
		GPIO.output(15, False)
	if key == 'z':
		print("Going backward!")
		GPIO.output(13, False)
		GPIO.output(15, True)

	if key == 'i':
		print("Going left!")
		GPIO.output(7, True)
		GPIO.output(11, False)
	if key == 'o':
		print("Stationary!")
		GPIO.output(7, False)
		GPIO.output(11, False)
	if key == 'p':
		print("Going backward!")
		GPIO.output(7, False)
		GPIO.output(11, True)
