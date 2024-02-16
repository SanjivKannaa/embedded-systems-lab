# when the button is released -> all the LEDs are off
# whem the button is pressed -> all the LEDs are on

import RPi.GPIO as GPIO
import time

buttonpin = 16
GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setmode(GPIO.BCM)
ledpin = [3, 5, 7, 8]
for i in ledpin:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
try:
    while True:
        GPIO.wait_for_edge(buttonpin, GPIO.FALLING)
        for i in ledpin:
            GPIO.output(i, GPIO.HIGH)
        time.sleep(1)
        GPIO.wait_for_edge(buttonpin, GPIO.RISING)
        for i in ledpin:
            GPIO.output(i, GPIO.LOW)
        time.sleep(1)
except:
    print("exiting")
GPIO.clearup()