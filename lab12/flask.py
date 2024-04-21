from flask import Flask, render_template, jsonify
import RPi.GPIO as gpio
import time

app = Flask(__main__)
gpio.setmode(gpio.BCM)
pins = [1, 2, 3]
gpio.setmode(gpio.BCM)
for i in pins:
    gpio.setup(i, gpio.LOW)

@app.get("/")
def hello():
    return render_template("home.html")

@app.get("/ledon1")
def ledon():
    try:
        gpio.output(pins[0], gpio.HIGH)
        return "1"
    except:
        return "0"
@app.get("/ledoff1")
def ledoff():
    try:
        gpio.output(pins[0], gpio.LOW)
        return "1"
    except:
        return "0"


@app.get("/ledon2")
def ledon():
    try:
        gpio.output(pins[1], gpio.HIGH)
        return "1"
    except:
        return "0"
@app.get("/ledoff2")
def ledoff():
    try:
        gpio.output(pins[1], gpio.LOW)
        return "1"
    except:
        return "0"


@app.get("/ledon3")
def ledon():
    try:
        gpio.output(pins[2], gpio.HIGH)
        return "1"
    except:
        return "0"
@app.get("/ledoff3")
def ledoff():
    try:
        gpio.output(pins[2], gpio.LOW)
        return "1"
    except:
        return "0"


app.run(host="0.0.0.0", port=5000)