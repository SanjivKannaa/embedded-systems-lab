# for every switch -> the intensity between both LEDs will change alternatively
import RPi.GPIO as GPIO
import time

buttonpin = 16
GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setmode(GPIO.BCM)
ledpin = [3, 5, 7, 8]
for i in ledpin:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
pwm = [None, None, None, None]
for i in range(4):
    pwm[i] = GPIO.PWM(ledpin[i], 100)
    if i%2==0:
        pwm[i].start(0)
    else:
        pwm[i].start(100)
try:
    while True:
        GPIO.wait_for_edge(buttonpin, GPIO.FALLING)
        for i in range(0, 100, 5):
            for j in range(len(pwm)):
                if j%2==0:
                    j.ChangeDutyCycle(i)
                else:
                    j.ChangeDutyCycle(100-i)
            time.sleep(1)
        GPIO.wait_for_edge(buttonpin, GPIO.RISING)
        for i in range(100, 0, -5):
            for j in range(len(pwm)):
                if j%2==0:
                    j.ChangeDutyCycle(i)
                else:
                    j.ChangeDutyCycle(100-i)
            time.sleep(1)
except:
    print("exiting")
GPIO.clearup()