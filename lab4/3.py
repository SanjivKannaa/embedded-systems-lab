'''
first click -> 1st LED goes up
second click -> 2nd LED goes up
third click -> 2nd LED goes down
fourth click -> 1st LED goes down
'''

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
        i = 0
        while i<len(ledpin):
            GPIO.wait_for_edge(buttonpin, GPIO.FALLING)
            GPIO.output(i, GPIO.HIGH)
            # time.sleep(1)
            i+=1
            GPIO.wait_for_edge(buttonpin, GPIO.RISING)
            GPIO.output(i, GPIO.HIGH)
            i+=1
        while i>=0:
            GPIO.wait_for_edge(buttonpin, GPIO.FALLING)
            GPIO.output(i, GPIO.LOW)
            # time.sleep(1)
            i-=1
            GPIO.wait_for_edge(buttonpin, GPIO.RISING)
            GPIO.output(i, GPIO.LOW)
            i-=1
except:
    print("exiting")
GPIO.clearup()