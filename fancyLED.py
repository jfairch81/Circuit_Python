# Jude Fairchild
# Have multiple LED's perform different actions
# 10/2/19

import time #pylint: disable-msg=import-error
import board #pylint: disable-msg=import-error
from digitalio  import Direction, Pull, DigitalInOut #pylint: disable-msg=import-error
import random

class FancyLED: # I used a class because I called it in "main FancyLED" and that is how it knows what all the variablees are and how to run them.

    def __init__(self,p1,p2,p3): #this defines and Initializes p1,p2,p3

        self.p1 = DigitalInOut(p1) #How I get p1 to be an LED
        self.p1.direction = Direction.OUTPUT

        self.p2 = DigitalInOut(p2)
        self.p2.direction = Direction.OUTPUT

        self.p3 = DigitalInOut(p3)
        self.p3.direction = Direction.OUTPUT  
    
    def alternate(self): # Alternate - It changes between the lights in a 1-2-1 pattern
        self.p1.value = True
        self.p2.value = False
        self.p3.value = True
        time.sleep(.25)

        self.p1.value = False
        self.p2.value = True
        self.p3.value = False
        time.sleep(.25)
        self.p2.value = False

    def blink(self): # Blink - It changes from On to Off
        self.p1.value = True
        self.p2.value = True
        self.p3.value = True
        time.sleep(.25)
        self.p1.value = False
        self.p2.value = False
        self.p3.value = False

    def on(self): # This was my test variable which turned everything on
        self.p1.value = True
        self.p2.value = True
        self.p3.value = True
    
    def chase(self): # This starts and has the led essentially move across the screen and turn off
        self.p1.value = True
        time.sleep(.25)
        self.p1.value = False
        self.p2.value = True
        time.sleep(.25)
        self.p2.value = False
        self.p3.value = True
        time.sleep(.25)
        self.p3.value = False
    
    def sparkle(self): # I used a randomizer to random from 1 - 3 and have that determine whether the light turns on or not
        n = random.randint(1,3)

        if n == 1: # If the random number is 1 then only the first light turns on
            self.p1.value = True
            self.p2.value = False
            self.p3.value = False
            time.sleep(.15)
        
        if n == 2:
            self.p1.value = False
            self.p2.value = True
            self.p3.value = False
            time.sleep(.15)
        
        if n == 3:
            self.p1.value = False
            self.p2.value = False
            self.p3.value = True
            time.sleep(.15)
