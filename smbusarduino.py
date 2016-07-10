import smbus import time import requests import datetime import RPi.GPIO 
bus = smbus.SMBus(1) 
SLAVE_ADDRESS = 0x04
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
RUNSTATE =False

def getMoisture():
    return int(bus.read_byte(SLAVE_ADDRESS))

def uploadMoisture(moist):
    #trying to get this url ready on the cloud would take some time
    url = "http://gradenpyapi.azurewebsites.net/soil/condition"
    task ={"Stamp":datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%dT%H:%M:%S"), "MoistureContent":moist}
    resp = requests.post(url, data=task)
    if resp.status_code ==201:
        #would have to as the arduino to light up the led and switch off
        print("just uploaded the moisture content")
        bus.write_byte(SLAVE_ADDRESS, 200)
        time.sleep(2)
        bus.write_byte(SLAVE_ADDRESS,0)
    else:
        bus.write_byte(SLAVE_ADDRESS,0)
print("Now starting the program ..")
while RUNSTATE ==False
	#here the program would have to wait for the push switch to start
	pushSwitch = GPIO.input(18)
	if pushSwitch ==False:
		RUNSTATE =True
		while True:
		    moisture =getMoisture()
		    print(moisture)
		    uploadMoisture(moisture)
		    time.sleep(60)
	else:
		#continue looking for the user trigger
		RUNSTATE =False
	
    
        
        
        
