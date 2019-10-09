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

r = 0
g = 0
b = 0

sonar = adafruit_hcsr04.HCSR04(trigger_pin = board.D12, echo_pin = board.D11)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)



while True:


    try: #Essentially works as an if/else statement for Distance Sensor
         # If it can read it then it will print the distance, otherwise it will print "Popeyes"
        print((sonar.distance,)) #Prints the distance in the Serial Monitor
        if sonar.distance <= 20: #I used 20 because the green both goes up and comes down from 35 to 20

            r = simpleio.map_range(sonar.distance, 0,20,255,0)
            b = simpleio.map_range(sonar.distance, 5,20,0,255)
            g = simpleio.map_range(sonar.distance, 20,35,0,255)

        else:
            r = simpleio.map_range(sonar.distance, 0,20,255,0)
            b = simpleio.map_range(sonar.distance, 35,20,0,255) #I mapped the Sonar Range and the RGB from 0 - 255
            g = simpleio.map_range(sonar.distance, 20,35,0,255)

        dot.fill((int(r),int(g),int(b))) #Code for the LED colors on the Metro Express
    except RuntimeError:
        print("Popeyes")

    time.sleep(0.1)

