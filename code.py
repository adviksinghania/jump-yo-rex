# code.py
"""
Project Name: Jump Yo' Rex
Author: Advik Singhania
Created On: 28th November, 2020; 07:48 PM IST

Make sure to copy the adafruit_hid library folder and
adafruit_lis3dh to the /lib folder of your CIRCUITPY drive.
I've connected a red LED to pin D4 to indicate jumps and
a blue LED to pin D0 to indicate ducks.
This source code has been tested for Seeeduino Xiao and can also work on CircuitPython supported boards.
"""

import time
import board
import digitalio
import busio
import adafruit_lis3dh
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Configurnig pins for the SPI connection:
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = digitalio.DigitalInOut(board.D5)  # Set to appropriate CS pin!
int1 = digitalio.DigitalInOut(board.D6)  # Set to correct pin for interrupt!
lis3dh = adafruit_lis3dh.LIS3DH_SPI(spi, cs, int1=int1)

# Initializing Keyboard:
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

time.sleep(1)

# Setting up LEDs for Jump(ledj) and Duck(ledd)
ledj = digitalio.DigitalInOut(board.D4)
ledj.direction = digitalio.Direction.OUTPUT
ledd = digitalio.DigitalInOut(board.D0)
ledd.direction = digitalio.Direction.OUTPUT

# Printing is for debugging, you can comment the print statements if you want.
print("Waiting for action...")
while True:
    ledj.value = False  # Turning Off LEDs
    ledd.value = False

    x, y, z = lis3dh.acceleration  # Getting values for the acceleration in x, y and z axes
    x, y, z = abs(x), abs(y), abs(z)  # Taking the absolute of the values since the change in relative acceleration will always be positive
    # print(x, y, z)

    # Setting up default position:
    if 8 < x < 10:
        pos = x
    elif 8 < z < 10:
        pos = z
    else:
        pos = y

    # Detecting jumps and ducks:
    if pos > 11:  # You can change these values according to your sensitivity
        print(x, y, z)
        keyboard.press(Keycode.UP_ARROW)  # "Press"...
        keyboard.release_all()
        print('Jumped')
        ledj.value = True
        time.sleep(0.5)
    elif pos < 8:  # You can change these values according to your sensitivity
        print(x, y, z)
        keyboard.press(Keycode.DOWN_ARROW)  # "Press"...
        print('Ducked')
        ledd.value = True
        time.sleep(0.5)
        keyboard.release_all()
        time.sleep(0.5)

    time.sleep(0.05)
