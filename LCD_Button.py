# Jude Fairchild
# LCD Button Monitor
# 8/30/19
import board #pylint: disable-msg=import-error
#import neopixel
import math #pylint: disable-msg=import-error
import time #pylint: disable-msg=import-error
import digitalio #pylint: disable-msg=import-error
import adafruit_bus_device #pylint: disable-msg=import-error

from lcd.lcd import LCD #pylint: disable-msg=import-error
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface #pylint: disable-msg=import-error

from lcd.lcd import CursorMode #pylint: disable-msg=import-error

lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)

inputPin = digitalio.DigitalInOut(board.D9) # This is how I got the button to work in Adafruit CircuitPython
inputPin.direction = digitalio.Direction.INPUT
inputPin.pull = digitalio.Pull.UP

button = digitalio.DigitalInOut(board.D8) # This is how got the switch to work in Adafruit CircuitPython
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

counter = 0 # Simple varriables I used
oldSwitchState = 0
newSwitchState = 1
adder = 1
while True:

    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Popeyes Line: ") #Prints this then how many people are in the "Popeyes Line: "

    lcd.set_cursor_pos(1,0)
    lcd.print(str(counter)) #Prints the counter on the LCD Screen

    if button.value:
        print("0")
        time.sleep(0.05)
        oldSwitchState = 0 #sets it to run the Elif by making oldSwitchState 0


    elif oldSwitchState == 0 and newSwitchState == 1:
        if inputPin.value:
            adder = 1 #adds to the adder which is then sets the counter to adder +1
        else:
            adder = -1
        print("1")
        print(str(adder)) # Prints the adder to the serial monitor
        time.sleep(0.05)
        counter += adder
        oldSwitchState = 1 #sets the oldSwitchState back to 1 which should not run the Elif