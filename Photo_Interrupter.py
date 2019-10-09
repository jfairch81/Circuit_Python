# Jude Fairchild
# 9/4/19
# Make a Photo Interrupter register every 4 seconds without using sleep function
import board #pylint: disable-msg=import-error
import math #pylint: disable-msg=import-error
import digitalio #pylint: disable-msg=import-error
import time #pylint: disable-msg=import-error
import adafruit_bus_device #pylint: disable-msg=import-error
Interrupts = -1 # For some reason I had to set it to -1 because 0 wasn't working rigt
photoPin = digitalio.DigitalInOut(board.D9)
photoPin.direction = digitalio.Direction.INPUT
photoPin.pull = digitalio.Pull.UP
fread = True # Fread and Lread are variables used for the Boolean Statement
lread = True
initial = time.monotonic() # I wasn't allowed to use time.sleep so I had to figure out how to use monotonic

while True:
    now = time.monotonic()
    if now - initial == 4: # Sets it = to 4 so it prints every 4 seconds
        print("The number of Interrupts is: " + str(Interrupts)) # Prints the number of interrupts every 4 seconds
        initial = time.monotonic()

    if photoPin.value:
        lread = True 



    else:
        if fread == lread:
            Interrupts += 1 # If it registers then it will count +1 as an interrupt
            lread = not lread