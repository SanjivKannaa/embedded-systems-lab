import smbus
import time
# Define LCD parameters
LCD_WIDTH = 16  # Maximum characters per line
# Define some device parameters
I2C_ADDR = 0x27  # I2C device address
LCD_CHR = 1  # Mode - Sending data
LCD_CMD = 0  # Mode - Sending command
LCD_LINE_1 = 0x80  # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  # LCD RAM address for the 2nd line
LCD_BACKLIGHT = 0x08  # On
# LCD_BACKLIGHT = 0x00  # Off
ENABLE = 0b00000100  # Enable bit
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
# Open I2C interface
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1
def lcd_byte(bits, mode):
    # Send byte to data pins
    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT
    # High bits
    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)
    # Low bits
    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    # Toggle enable
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
    time.sleep(E_DELAY)

def lcd_string(message, line):
    # Send string to display
    message = message.ljust(LCD_WIDTH, " ")

    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

if __name__ == '__main__':
    try:
        while True:
            lcd_string("Hello, World!", LCD_LINE_1)
            lcd_string("Raspberry Pi", LCD_LINE_2)

            time.sleep(2)  # 2 second delay

            lcd_string("LCD Interfacing", LCD_LINE_1)
            lcd_string("with Python", LCD_LINE_2)

            time.sleep(2)  # 2 second delay

    except KeyboardInterrupt:
        pass

    finally:
        lcd_string("", LCD_LINE_1)
        lcd_string("", LCD_LINE_2)

        time.sleep(2)