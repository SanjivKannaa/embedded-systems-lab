import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
led_pin = [3, 5, 7, 8]
GPIO.setup(led_pin[0], GPIO.OUT)
GPIO.setup(led_pin[1], GPIO.OUT)
GPIO.setup(led_pin[2], GPIO.OUT)
GPIO.setup(led_pin[3], GPIO.OUT)
try:
    while True:
        i = random.randint(0, 3)
        GPIO.output(led_pin[i], GPIO.HIGH)
        print("LED {} is ON".format(i+1))
        time.sleep(1)
        GPIO.output(led_pin[i], GPIO.LOW)
except KeyboardInterrupt:
    print("exiting")
except Exception as e:
    print("error", e)
GPIO.cleanup()