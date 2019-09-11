# Jude Fairchild
# LCD Button Monitor
# 8/30/19
import board
#import neopixel
import math
import time
import digitalio
import adafruit_bus_device

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode

lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)

inputPin = digitalio.DigitalInOut(board.D9)
inputPin.direction = digitalio.Direction.INPUT
inputPin.pull = digitalio.Pull.UP

button = digitalio.DigitalInOut(board.D8)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

counter = 0
oldSwitchState = 0
newSwitchState = 1
adder = 1
while True:

    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Popeyes Line: ")

    lcd.set_cursor_pos(1,0)
    lcd.print(str(counter))

    if button.value:
        print("0")
        time.sleep(0.05)
        oldSwitchState = 0


    elif oldSwitchState == 0 and newSwitchState == 1:
        if inputPin.value:
            adder = 1
        else:
            adder = -1
        print("1")
        print(str(adder))
        time.sleep(0.05)
        counter += adder
        oldSwitchState = 1