import smbus
import time

LCD_WIDTH = 16
I2C_ADDR = 0x27
LCD_CHR = 1
LCD_CMD = 0
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0
LCD_BACKLIGHT = 0x08
ENABLE = 0b00000100
E_PULSE = 0.0005
E_DELAY = 0.0005
bus = smbus.SMBus(1)
def lcd_byte(bits, mode):
    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT
    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)
    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)
def lcd_toggle_enable(bits):
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
    time.sleep(E_DELAY)
def lcd_string(message, line):
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, LCD_CMD)
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)
if __name__ == '__main__':
    try:
        while True:
            lcd_string("Hello, World!", LCD_LINE_1)
            lcd_string("Raspberry Pi", LCD_LINE_2)
            time.sleep(2)
            lcd_string("LCD Interfacing", LCD_LINE_1)
            lcd_string("with Python", LCD_LINE_2)
            time.sleep(2)
    except KeyboardInterrupt:
        pass
    finally:
        lcd_string("", LCD_LINE_1)
        lcd_string("", LCD_LINE_2)
        time.sleep(2)
