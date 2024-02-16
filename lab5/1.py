# displaying digits
# digits from 0 to 9 are displayed on the 7 segment display


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
arr = [
    [1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1]
]

x = [3, 5, 11, 15, 19, 18, 22]
for i in x:
    GPIO.setup(i, GPIO, initial=GPIO.LOW)
try:
    while True:
        for num in arr:
            for i in range(7):
                if num[i]==1:
                    GPIO.output(x[i], GPIO.HIGH)
            time.sleep(1.2)
            for i in range(7):
                GPIO.output(x[i], GPIO.LOW)
except:
    print("exiting")
GPIO.cleanup()