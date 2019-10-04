# Jude Fairchild
# Use a distance sensor to change colors of an RGB LED
# 9/11/19

import board #pylint: disable-msg=import-error
import time #pylint: disable-msg=import-error
import digitalio #pylint: disable-msg=import-error
import adafruit_bus_device #pylint: disable-msg=import-error
import adafruit_hcsr04 #pylint: disable-msg=import-error
import neopixel #pylint: disable-msg=import-error
import simpleio #pylint: disable-msg=import-error

r = 0 #Red Green and Blue variables for the RGB LED on the board
g = 0
b = 0

sonar = adafruit_hcsr04.HCSR04(trigger_pin = board.D12, echo_pin = board.D11) #This is how you get HC-SR04 on Adafruit
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)



while True:


    try:
        print((sonar.distance,))
        if sonar.distance <= 20:

            r = simpleio.map_range(sonar.distance, 0,20,255,0) # Mapping the LED for the distance and the RGB
            b = simpleio.map_range(sonar.distance, 5,20,0,255)
            g = simpleio.map_range(sonar.distance, 20,35,0,255)

        else:
            r = simpleio.map_range(sonar.distance, 0,20,255,0)
            b = simpleio.map_range(sonar.distance, 35,20,0,255)
            g = simpleio.map_range(sonar.distance, 20,35,0,255)

        dot.fill((int(r),int(g),int(b))) #Fills the Red Green and Blue to the distance mapped
    except RuntimeError:
        print("Popeyes")

    time.sleep(0.1)

