# Jude Fairchild
# Turn an RGB LED different colors using code
# 9/25/19

import simpleio #pylint: disable-msg=import-error
import pulseio #pylint: disable-msg=import-error
import time #pylint: disable-msg=import-error

class RGB:
    kind="colors"
    def __init__(self, r, g, b): # Initializing variable for R, G, and B
        self.pwm_r = pulseio.PWMOut(r, frequency=1000, duty_cycle=0) # I used PWM pins because the work with rainbow a lot better
        self.pwm_g = pulseio.PWMOut(g, frequency=1000, duty_cycle=0)
        self.pwm_b = pulseio.PWMOut(b, frequency=1000, duty_cycle=0)

    def change_name(self, newName):
        self.name = newName

    def change_pins(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def red(self): # 2**16-1 basically means off and 0 means on so only red is on
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 2**16-1


    def blue(self): # Only blue is on
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 0


    def magenta(self): # Magenta is a mix between red and blue so both are on
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 0


    def green(self): # Only green is on
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 2**16-1


    def yellow(self): # Yellow is a mix between Red and Green so both are on
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 2**16-1

    def cyan(self): # Cyan is a mix between green and blue so both are on
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 0

    def rainbow(self): # Rainbow switches from all colors smoothly 
        for i in range(0,2**16-1,128): # Mapped it so it can transfer smoothly
            self.pwm_r.duty_cycle = 0 + i # maxing less and less red
            self.pwm_g.duty_cycle = 2**16-1 - i # making more and more green
            self.pwm_b.duty_cycle = 2**16-1
            time.sleep(0.005)
        for i in range(0,2**16-1,128):
            self.pwm_r.duty_cycle = 2**16-1
            self.pwm_g.duty_cycle = 0 + i
            self.pwm_b.duty_cycle = 2**16-1 - i
            time.sleep(0.005)
        for i in range(0,2**16-1,128):
            self.pwm_r.duty_cycle = 2**16-1 - i
            self.pwm_g.duty_cycle = 2**16-1
            self.pwm_b.duty_cycle = 0 + i
            time.sleep(0.005)

    def rainbow2(self): # Basically rainbow but it goes at a different speed
        for i in range(0,2**16-1,128):
            self.pwm_r.duty_cycle = 0 + i
            self.pwm_g.duty_cycle = 2**16-1 - i
            self.pwm_b.duty_cycle = 2**16-1
            time.sleep(0.001)
        for i in range(0,2**16-1,128):
            self.pwm_r.duty_cycle = 2**16-1
            self.pwm_g.duty_cycle = 0 + i
            self.pwm_b.duty_cycle = 2**16-1 - i
            time.sleep(0.001)
        for i in range(0,2**16-1,128):
            self.pwm_r.duty_cycle = 2**16-1 - i
            self.pwm_g.duty_cycle = 2**16-1
            self.pwm_b.duty_cycle = 0 + i
            time.sleep(0.001)






