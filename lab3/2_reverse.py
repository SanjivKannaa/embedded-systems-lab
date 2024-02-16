import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
frequency = 100
duty_cycle = 0
led_pin = [3, 5, 7, 8]
for i in range(4):
    GPIO.setup(led_pin[i], GPIO.OUT)
pwm = [None, None, None, None]
for i in range(4):
    pwm[i] = GPIO.PWM(led_pin[i], frequency)
    pwm[i].start(duty_cycle)

try:
    while True:
        for i in range(4)[::-1]:   
            print("LED NO = {}".format(i+1))
            for dc in range(0, 100, 5):
                pwm[i].ChangeDutyCycle(dc)
                time.sleep(1)
            for dc in range(100, 0, -5):
                pwm[i].ChangeDutyCycle(dc)
                time.sleep(1)        
except KeyboardInterrupt:
    print("exiting")
except Exception as e:
    print("error", e)
for i in range(4):
    pwm[i].stop()
GPIO.cleanup()