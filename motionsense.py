#this is to take inputs from the PIr sensors detecting the motion change

import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

#this is to get the user parameters
pinInput  = input("PIR @ pin :")
pirPin  = int(pinInput)
gpio.setup(pirPin, gpio.IN)
#getting the led pin since we want the led to light up when the motion is detected
pinOutput = input("LED @ pin")
if int(pinOutput) > 0:
	ledPin = int(pinOutput)
	gpio.setup(ledPin, OUT)
	gpio.output(ledPin,False)

#this would just take the user input and adjust the brightness if the led on the scale of 0-100
while True:
	if gpio.input(pirPin) ==False:
		print("..")
		gpio.output(ledPin, False)
		#wait time for the 2 conditions is differential
		time.sleep(0.2)
	else:
		print("Motion detected")
		gpio.output(ledPin, True)
		time.sleep(1)
	