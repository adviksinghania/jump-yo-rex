# Jump-Yo'-Rex
This repo is for my Jump Yo' Rex project.

_You jump and your Rex jumps with you, you duck and your Rex ducks with you._

## Seeduino XIAO
The SEEED Studio's [Seeeduino XIAO](https://wiki.seeedstudio.com/Seeeduino-XIAO/) is a minimal, low-cost board that uses the Atmel ATSAMD21G18, a powerful 32-bit ARM Cortex®-M0+ processor running at 48MHz with 256KB Flash and 32KB SRAM. The board is 20 x 17.5mm in size which is perfect for wearable devices and small projects. It has multiple development interfaces including DAC output, SWD Bonding pad interface, I2C, UART and SPI interfaces. It's Compatible with both [Arduino IDE](https://www.arduino.cc) and [CircuitPython](https://www.circuitpython.org) and uses a USB-C connector.

## Setup
* Get started with [CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython) if you haven't already. Install [Mu](https://codewith.mu/) on your PC.
* Make sure that you're running the latest version of CircuitPython on the board you're using. More info can be found [here](https://wiki.seeedstudio.com/Seeeduino-XIAO-CircuitPython/), [there](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython) and [everywhere](https://learn.adafruit.com/welcome-to-circuitpython/troubleshooting).
* Unzip the lib.zip and copy the libraries on your CIRCUITPY drive.
* Copy and paste the source code from code.py to your code.py in CIRCUITPY drive.
* Disconnect the board and wire your components according to the diagram below:
![Schematic](https://github.com/adviksinghania/jump-yo-rex/blob/main/schematic.png?raw=true)

## Play
* This works best when you disconnect from the internet and play on your Chrome browser, instead of going to a third party site.
* **Before connecting the setup to your PC, note that this project uses the UP or DOWN arrow keys when it detects a jump or a duck. So make sure you don't have a window open that can harm your work.**
* Attach the project to your body using a slim belt (don't press too hard).
* This is designed to work in all directions but works best if the Y-axis is pointing downwards.
* Connect the USB Cable and open Chrome after disconnecting from the internet.
* The accelerometer should detect change in acceleration and blink the red LED for a jump and a blue LED for a duck.
* So now, you'll have to exercise a lot :)
