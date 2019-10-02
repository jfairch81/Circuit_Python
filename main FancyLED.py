import time #pylint: disable-msg=import-error
import board #pylint: disable-msg=import-error
from digitalio  import Direction, Pull, DigitalInOut #pylint: disable-msg=import-error
from fancyLED import FancyLED

fancy1 = FancyLED(board.D2,board.D3,board.D4)
fancy2 = FancyLED(board.D5,board.D6,board.D7)




fancy1.alternate()
time.sleep(1)
fancy2.blink()
time.sleep(1)
fancy1.chase()
time.sleep(1)

while True:
    fancy2.sparkle()