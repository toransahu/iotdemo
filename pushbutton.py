import RPi.GPIO as gpio
import time

#this is where we make the setup
gpio.setmode(gpio.BOARD)
#this is that we are setting the gpio pin to a suitable mode on the pi board
gpio.setup(18, gpio.IN, pull_up_down=gpio.PUD_UP)

while True:
	switchStatus = gpio.input(18)
	if switchStatus ==False:
		#this is the case when the button was detected to be pressed by the user
		print("Ping! - button is pressed , we can start the program")
		time.sleep(0.2)
	else:
		print("button is not pressed")
		time.sleep(0.2)

	
