# Jude Fairchild
# Servo Touch
# 8/26/19

import time #pylint: disable-msg=import-error
import board #pylint: disable-msg=import-error
import pulseio #pylint: disable-msg=import-error
from adafruit_motor import servo #pylint: disable-msg=import-error
import touchio #pylint: disable-msg=import-error
import digitalio #pylint: disable-msg=import-error


pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50) # create a PWMOut object on Pin A2.


my_servo = servo.Servo(pwm) # Create a servo object, my_servo.

Servo_Angle = 0


touch_A1 = touchio.TouchIn(board.A1)  # Not a touch pin on Trinket M0!
touch_A2 = touchio.TouchIn(board.A2) 

while True:


    if touch_A1.value and Servo_Angle < 180: #Stating that that if the wire connected to A1 is touched and it is less than 180, it will turn the servo
        print("Touched A1!") # Prints to the Serial Monitor
        Servo_Angle += 1 # Turns the angle by a designated variable which for me is 1
        my_servo.angle = Servo_Angle # Sets my variable "Servo_Angle" to the actual servo variable


    time.sleep(0.001)

    if touch_A2.value and Servo_Angle > 0: 
        print("Touched A2!")
        Servo_Angle -= 1
        my_servo.angle = Servo_Angle

    time.sleep(0.001)