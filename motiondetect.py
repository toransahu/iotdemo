#this is the experiment on motion detection using the PIR sensor
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

ip_pin = input("Enter the pin where the PIR is connected: ")
pirPin = int(ip_pin)

gpio.setup(pirPin, gpio.IN)

while True:
    signal = gpio.input(pirPin)
    if(signal==True):
        print("Motion detected")
        time.sleep(1)
    else:
        print("..")
        time.sleep(0.2)
    
    
    
