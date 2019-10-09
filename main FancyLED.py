# Jude Fairchild
# The main code for FancyLED
# 10/2/19

import time #pylint: disable-msg=import-error
import board #pylint: disable-msg=import-error
from digitalio  import Direction, Pull, DigitalInOut #pylint: disable-msg=import-error
from fancyLED import FancyLED

fancy1 = FancyLED(board.D2,board.D3,board.D4) # These are the Three pins I used for Fancy1
fancy2 = FancyLED(board.D5,board.D6,board.D7) # These are the Three pins I used for Fancy2




fancy1.alternate() # Theese are Variables that he Assigned
time.sleep(1)
fancy2.blink()
time.sleep(1)
fancy1.chase()
time.sleep(1)

while True:
    fancy2.sparkle() # The reasoning for putting this in the While True is it randomizes and is easier to see the random variables when it is in the While True