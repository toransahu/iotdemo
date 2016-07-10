#this file is reset the specific pins to not deliver output

import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

while True:
    user_ip = input("Enter the pin that you want to shut off: ")
    pin = int(user_ip)
    gpio.setup(pin, gpio.OUT)
    gpio.output(pin, False)
    print("Your pin is shut off now")
    
