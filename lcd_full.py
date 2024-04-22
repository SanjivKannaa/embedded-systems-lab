from Adafruit_CharLCD import Adafruit_CharLCD # Importing Adafruit library for LCD
from time import sleep # Importing sleep from time library to add delay in program
# initiate lcd and specify pins
lcd = Adafruit_CharLCD (rs=26, en=19, d4=13, d5=6, d6=5, d7=21, cols=16, lines=2)
lcd.clear()
# display text on LCD, \n = new line
lcd.message('WELCOME TO \nIoT STARTERS')
sleep(2)
# scroll text on display
try:
     while 1:
for x in range(0, 16):
lcd.move_left()
sleep(0.1)
sleep(1)
# scroll Right
for x in range(0, 16):
lcd.move_right()
sleep(0.1)
sleep(3)
# If Keyboard Interrupt command is pressed
except KeyboardInterrupt:
pass
# Clear the screen
lcd.clear()