import time #pylint: disable-msg=import-error
import board #pylint: disable-msg=import-error
from digitalio  import Direction, Pull, DigitalInOut #pylint: disable-msg=import-error
import random

class FancyLED:

    def __init__(self,p1,p2,p3):

        self.p1 = DigitalInOut(p1)
        self.p1.direction = Direction.OUTPUT

        self.p2 = DigitalInOut(p2)
        self.p2.direction = Direction.OUTPUT

        self.p3 = DigitalInOut(p3)
        self.p3.direction = Direction.OUTPUT  
    
    def alternate(self):
        self.p1.value = True
        self.p2.value = False
        self.p3.value = True
        time.sleep(.25)

        self.p1.value = False
        self.p2.value = True
        self.p3.value = False
        time.sleep(.25)
        self.p2.value = False

    def blink(self):
        self.p1.value = True
        self.p2.value = True
        self.p3.value = True
        time.sleep(.25)
        self.p1.value = False
        self.p2.value = False
        self.p3.value = False

    def on(self):
        self.p1.value = True
        self.p2.value = True
        self.p3.value = True
    
    def chase(self):
        self.p1.value = True
        time.sleep(.25)
        self.p1.value = False
        self.p2.value = True
        time.sleep(.25)
        self.p2.value = False
        self.p3.value = True
        time.sleep(.25)
        self.p3.value = False
    
    def sparkle(self):
        n = random.randint(1,3)

        if n == 1:
            self.p1.value = True
            self.p2.value = False
            self.p3.value = True
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
