#this is to have blinky led work for us
import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
# the other one is gpio.BCM which means you are refering to the pins by the broadcom soc channel
# BCM is already archived and no longer used  after pi model b, neither are they going to use it in future
gpio.setmode(gpio.BOARD)
#getting the choice of the user pin
ui = input("Enter the pin where the led is connected :")
ledPin = int(ui)

blink  = input("Enter the blink duration (secs) :")
blinkSecs = int(blink)

cutoff = input("Enter the number of times to blink: ")
overflow = int(cutoff)

# this is where we set the direction of the pin
# in this case ledpin is the output pin (Rpi is controlling this pin)
gpio.setup(ledPin, gpio.OUT)

while overflow >0:
    gpio.output(ledPin, True)
    time.sleep(blinkSecs)
    gpio.output(ledPin, False)
    overflow -=1
    time.sleep(blinkSecs)
    


