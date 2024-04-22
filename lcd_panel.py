from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep
lcd = Adafruit_CharLCD (rs=26, en=19, d4=13, d5=6, d6=5, d7=21, cols=16, lines=2)
lcd.clear()
lcd.message('WELCOME TO \nIoT STARTERS')
sleep(2)


'''
VSS GND
VDD 5V
contrast GND
RS GPIO26
RW GND
E GPIO19
D0 
D1 
D2 
D3 
D4 GPIO13
D5 GPIO6
D6 GPIO5
D7 GPIO21
backligt cathode
backligt cathode
'''