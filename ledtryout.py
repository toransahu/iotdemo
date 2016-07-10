import RPi.GPIO as gpio
import time
#this is where we do the set up
gpio.setwarnings(False)
user_input = input("Enter the GPIO pin at which the led is connected")
led_pin=int(user_input)
gpio.setmode(gpio.BOARD)
gpio.setup(led_pin,gpio.OUT)
#this is setting the frequency so the freq is 500Hz


led_pwm = gpio.PWM(led_pin, 500)
led_pwm.start(100)
#this is where we let the user enter some value and control brightness
while True:
    duty_s = input("enter the duty of the led: ")
    duty = int(duty_s)
    led_pwm.ChangeDutyCycle(duty)
    print("the led must have changed the brightness")



