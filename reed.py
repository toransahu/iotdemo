import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.IN)
GPIO.setup(7,GPIO.OUT)
count = 0
while(count<100):
	result = GPIO.input(5)
	if(result == 0):
		GPIO.output(7,0)
		time.sleep(0.10)
	elif(result == 1):
		GPIO.output(7,1)
		time.sleep(0.10)
	count = count + 1
GPIO.output(7,0)
