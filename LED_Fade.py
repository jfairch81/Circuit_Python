# Jude Fairchild
# Have an LED Fade in and out
# 8/22/19
# Adapted from Phillip's code


# Write your code here :-)
import board #pylint: disable-msg=import-error
import analogio #pylint: disable-msg=import-error

#dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

led = analogio.AnalogOut(board.A0)


while True:

    for i in range (31000,42000,1): # I use 31000 - 42000 because it shows the highest difference in LED lighting
        led.value = i

    for i in range (42000,31000,-1): # I found the way to make it fade out was to switch the direction of the 42 and 31 and then make it -1 not 1
        led.value = i