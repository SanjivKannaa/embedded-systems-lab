import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pir_pin = 17
buzzer_pin = 18
GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)
try:
    print("PIR Module Test (CTRL+C to exit)")
    time.sleep(2)
    print("Ready")
    while True:
        if GPIO.input(pir_pin):
            print("Motion detected!")
            GPIO.output(buzzer_pin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(buzzer_pin, GPIO.LOW)
        else:
            print("No motion detected")
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
