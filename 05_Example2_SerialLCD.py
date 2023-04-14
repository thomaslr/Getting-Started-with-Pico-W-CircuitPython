'''
Example 2 for Pi Pico W I2C LCD: Shifting
References:
  [1] https://github.com/Guitarman9119/Raspberry-Pi-Pico-/tree/main/I2C%2016x2%20LCD%20Circuit%20Python

Additional Library:
- lcd.py from [1]
- i2c_pcf8574_interface.py from [1]
'''
import board
import time
import busio
import digitalio
# Needs these 2 libraries from Guitarman9119 Github
# Upload it to the 'Lib'
import lcd
import i2c_pcf8574_interface

i2c = busio.I2C(scl=board.GP5, sda=board.GP4)
address = 0x27
i2c = i2c_pcf8574_interface.I2CPCF8574Interface(i2c, address)
display = lcd.LCD(i2c, num_rows=2, num_cols=16)
display.set_backlight(True)
display.set_display_enabled(True)

while True:
    display.clear()
    display.print("Example 2\nShifting")
    time.sleep(2)
    display.clear()
    # Shift Right
    for i in range(16):
        display.clear()
        display.set_cursor_pos(0, 0)
        display.print("->")
        display.shift_display(i)
        time.sleep(0.2)
    # Shift Left
    for j in reversed(range(16)):
        display.clear()
        display.set_cursor_pos(1, 0)
        display.print("<-")
        display.shift_display(j)
        time.sleep(0.2)
