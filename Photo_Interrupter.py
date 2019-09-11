# Jude Fairchild
# 9/4/19
# Make a Photo Interrupter register every 4 seconds without using sleep function
import board
import math
import digitalio
import time
import adafruit_bus_device
Interrupts = -1
photoPin = digitalio.DigitalInOut(board.D9)
photoPin.direction = digitalio.Direction.INPUT
photoPin.pull = digitalio.Pull.UP
fread = True
lread = True
initial = time.monotonic()

while True:
    now = time.monotonic()
    if now - initial == 4:
        print("The number of Interrupts is: " + str(Interrupts))
        initial = time.monotonic()

    if photoPin.value:
        lread = True



    else:
        if fread == lread:
            Interrupts += 1
            lread = not lread