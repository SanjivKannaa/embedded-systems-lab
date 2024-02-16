import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led_pin = [3, 5, 7, 8]
GPIO.setup(led_pin[0], GPIO.OUT)
GPIO.setup(led_pin[1], GPIO.OUT)
GPIO.setup(led_pin[2], GPIO.OUT)
GPIO.setup(led_pin[3], GPIO.OUT)
try:
    while True:
        for i in range(4)[::-1]:
            GPIO.output(led_pin[i], GPIO.HIGH)
            print("LED {} is ON".format(i+1))
            time.sleep(1)
            GPIO.output(led_pin[1], GPIO.LOW)
except KeyboardInterrupt:
    print("exiting")
except Exception as e:
    print("error", e)
GPIO.cleanup()