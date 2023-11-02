# Basic example of clearing and drawing pixels on a SSD1306 OLED display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Tony DiCola
# License: Public Domain

# Import all board pins.
#from board import SCL, SDA
import board
import busio

# Import the SSD1306 module.
import adafruit_displayio_ssd1306


# Create the I2C interface.
i2c = busio.I2C(scl=board.GP15, sda=board.GP14)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
display = adafruit_displayio_ssd1306.SSD1306(128, 64, 0)
#display = SSD1306_I2C(128, 64, i2c)

#64 or 32?

# Alternatively you can change the I2C address of the device with an addr parameter:
#display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x31)

# Clear the display.  Always call show after changing pixels to make the display
# update visible!
display.fill(0)

display.show()

# Set a pixel in the origin 0,0 position.
display.pixel(0, 0, 1)
# Set a pixel in the middle 64, 16 position.
display.pixel(64, 16, 1)
# Set a pixel in the opposite 127, 31 position.
display.pixel(127, 31, 1)
display.show()




while True:
    display.clear()
    display.set_cursor_pos(0, 0)
    display.print("CircuitPython\nI2C LCD")
    time.sleep(2)
    display.clear()
    display.set_cursor_pos(1, 0)
    display.print("Example = {:5.2f}".format(23.456))
    time.sleep(2)