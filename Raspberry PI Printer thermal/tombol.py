import subprocess
import RPi.GPIO as GPIO
import time
from escpos import *

BUTTON_PIN = 16
relay_pin = 20
GPIO.setmode (GPIO.BCM)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(relay_pin, GPIO.OUT)

previous_button_state = GPIO.input(BUTTON_PIN)


    
try:
    while True:
        time.sleep(0.01)
        button_state=GPIO.input(BUTTON_PIN)
        if button_state != previous_button_state:
            previous_button_state = button_state
            if button_state == GPIO.HIGH:
                GPIO.output(relay_pin, GPIO.LOW)
                print("button has released")
                subprocess.run(["python3", "/home/rvaldi26/main.py"])
            else:
                 GPIO.output(relay_pin, GPIO.HIGH)
            
                
except KeyboardInterrupt:
    GPIO.cleanup()
