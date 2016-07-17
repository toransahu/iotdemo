import time
# this is for serial communication
import smbus
import RPi.GPIO as GPIO
import datetime as dt
# this is for  uplinking the data to the cloud
import requests as http
# this is the address of the slave board i.e. arduino
'''
Since there can be multiple arduino slave boards  but each board has to be identified with unique address
'''
slave =0x04
# this is setting up the bus for communication
bus=smbus.SMBus(1)
# this measures the no. of unsuccessful attempts to connect to cloud
uplinkAttempt=0
GPIO.setmode(GPIO.BOARD)
# rhis is the interrupt button connection from the breadboard
interruptPin = 7
GPIO.setup(interruptPin, GPIO.IN, pull_up_down =GPIO.PUD_UP)
sleeper = 3
userReaction=3
# this is the led blink delay when the data is uploaded to the cloud
ledBlink =2

#task to upload the soil condition from arduino to cloud
def test_log_soilstate():
	reading = bus.read_i2c_block_data(slave,10)
	print("reading received from arduino")
	print(reading[0])
	print(reading[1])
	print(reading[2])
	print(reading[3])
	return True

def uplink_soil_condition():
	#getting the serial feed from arduino for the moisture content
	#this is where you read the values from arduino
	reading = bus.read_i2c_block_data(slave,10)
	# his is the service url
	url= "http://46.101.216.198/soilconditions"
	#this is the formatted timestamp of the information
	timestamp =dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%dT%H:%M:%S")
	#this is the actual data format which will be sent, closely resembling json
	#python dict
	data = {"stamp":timestamp, "moisture":reading[0]}
	#uploading now to azure
	#we do not know the index of the data parameter but that it's named parameter
	resp= http.post(url, data=data) 
	if (resp.status_code ==200 or resp.status_code==201):
		#notifying arduino, so led @13 is blinked for 1 sec
		bus.write_byte(slave,200)
		time.sleep(ledBlink)
		bus.write_byte(slave,0)
		return True
	else:
		return False
#this function just verifies if the user has hard-interrupted the process
def isInterrupted():
	pushButton = GPIO.input(interruptPin)
	# False here means that the pushbutton is pressed/interrupted
	if pushButton ==False:
		return True
	else:
		#window for the user to interrupt the soild reading process
		print("interrupt?")
		time.sleep(userReaction)
		#once again reading the GPIO input
		pushButton = GPIO.input(interruptPin)
		if pushButton ==False:
			#the user has used the window to interrupt
			return True
		else:
			#user would not want to interrupt
			return False

#this is the main function that runs the control
while (True and uplinkAttempt<20):
	if isInterrupted() ==False:
		print("uplinking soil condition..")
		uplink= uplink_soil_condition()
		if uplink ==True:
			print("soil condition uplinked")
			print("Next sample after sleeper seconds")
			time.sleep(sleeper) 
			#this is waiting for the next soil condition
		else:
			print("Error uploading data to server")
			uplinkAttempt +=1
	else:
		print("Interrupted..")
		time.sleep(ledBlink) #sleep and then read the interrupt button

print("Logging off..")
