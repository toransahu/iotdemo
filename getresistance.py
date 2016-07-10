#this is for measuring the resistance connected in series with input and ground

import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

#this gets the pin connections from the user
def PinConnections():
	uisupply  = input("Supply from pin #: ")
	psupply  = int(uisupply)
	uitest =input("Test from pin #: ")
	ptest  = int(uitest)
	return psupply, ptest

(pinSupply,pinTest)  = PinConnections()
#this would discharge the capacitor 
def DischargeCapitor ():
	#this is where we go ahead to set the reverse on the pins so that the capacitor is discharged
	gpio.setup(pinSupply, IN)
	gpio.setup(pinTest, OUT)
	gpio.output(pinTest,False)
	#wait for the capacitor to get discharged 
	time.sleep(0.005) #that is 5 miliseconds
#this would measure the charging time of the capacitor
def MeasureChargingTime():
	#here we have to setup the pins in the correct way to get working and measure the capacitance
	gpio.setup(pinSupply, OUT)
	gpio.setup(pinTest, IN)
	gpio.output(pinSupply,True)
	count = 0
	while gpio.input(pinTest) != True:
		count +=1
	return count
	
#and here is main loop that would let us measure the charging time
while True:
	DischargeCapitor()
	print(MeasureChargingTime())
	#wait for some time to do the next calculation
	time.sleep(0.5)#this is just safety net so that we dont get too many identical values
	