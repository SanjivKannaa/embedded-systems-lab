import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
trigger_pin = 23
echo_pin = 24
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)
try:
    while True:
        GPIO.output(trigger_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(trigger_pin, GPIO.LOW)
        while GPIO.input(echo_pin) == 0:
            pulse_start_time = time.time()
        while GPIO.input(echo_pin) == 1:
            pulse_end_time = time.time()
        pulse_duration = pulse_end_time - pulse_start_time
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        print("Distance:", distance, "cm")
        time.sleep(1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
