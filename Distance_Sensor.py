# Jude Fairchild
# Use a distance sensor to change colors of an RGB LED
# 9/11/19

import board
import time
import digitalio
import adafruit_bus_device
import adafruit_hcsr04
import neopixel
import simpleio

r = 0
g = 0
b = 0

sonar = adafruit_hcsr04.HCSR04(trigger_pin = board.D12, echo_pin = board.D11)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)



while True:


    try:
        print((sonar.distance,))
        if sonar.distance <= 20:

            r = simpleio.map_range(sonar.distance, 0,20,255,0)
            b = simpleio.map_range(sonar.distance, 5,20,0,255)
            g = simpleio.map_range(sonar.distance, 20,35,0,255)

        else:
            r = simpleio.map_range(sonar.distance, 0,20,255,0)
            b = simpleio.map_range(sonar.distance, 35,20,0,255)
            g = simpleio.map_range(sonar.distance, 20,35,0,255)

        dot.fill((int(r),int(g),int(b)))
    except RuntimeError:
        print("Popeyes")

    time.sleep(0.1)

