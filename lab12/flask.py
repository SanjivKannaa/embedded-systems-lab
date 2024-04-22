from flask import Flask, render_template
import RPi.GPIO as gpio
import time

app = Flask(__name__)
gpio.setmode(gpio.BCM)
pins = [1, 2, 3]
for i in pins:
    gpio.setup(i, gpio.LOW)

@app.get("/")
def hello():
    return render_template("home.html")

@app.get("/ledon1")
def ledon1():
    gpio.output(pins[0], gpio.HIGH)

@app.get("/ledoff1")
def ledoff():
    try:
        gpio.output(pins[0], gpio.LOW)
        return "1"
    except:
        return "0"



app.run(host="0.0.0.0", port=5000)