#this is to control the pulse width modulation using the raspberry inputs
#thus the brightness of the led can be controlled using the user inputs
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

#this is to get the user parameters
pinInput  = input("Led @ pin :")
ledPin = int(pinInput)
gpio.setup(ledPin, gpio.OUT)

ledPwm = gpio.PWm(ledPin,500)
ledPwm.start(100)

#this would just take the user input and adjust the brightness if the led on the scale of 0-100
while True:
	iplevel  = input("Enter the brightness value 0-100: ")
	level = int(iplevel)
	ledPwm.ChangeDutyCycle(level)