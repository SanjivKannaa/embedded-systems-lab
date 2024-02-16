import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
frequency = 100
duty_cycle = 0
led_pin = [3, 5, 7, 8]
GPIO.setup(led_pin[0], GPIO.OUT)
GPIO.setup(led_pin[1], GPIO.OUT)
GPIO.setup(led_pin[2], GPIO.OUT)
GPIO.setup(led_pin[3], GPIO.OUT)
pwm = [None, None, None, None]
pwm[0] = GPIO.PWM(led_pin[0], frequency)
pwm[0].start(duty_cycle)
pwm[1] = GPIO.PWM(led_pin[1], frequency)
pwm[1].start(duty_cycle)
pwm[2] = GPIO.PWM(led_pin[2], frequency)
pwm[2].start(duty_cycle)
pwm[3] = GPIO.PWM(led_pin[3], frequency)
pwm[3].start(duty_cycle)

try:
    while True:
        for i in range(4):   
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
pwm[0].stop()
pwm[1].stop()
pwm[2].stop()
pwm[3].stop()
GPIO.cleanup()