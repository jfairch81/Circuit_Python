# Jude Fairchild
# Servo Touch
# 8/26/19

import time
import board
import pulseio
from adafruit_motor import servo
import touchio
import digitalio

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

Servo_Angle = 0


touch_A1 = touchio.TouchIn(board.A1)  # Not a touch pin on Trinket M0!
touch_A2 = touchio.TouchIn(board.A2)

while True:


    if touch_A1.value and Servo_Angle < 180:
        print("Touched A1!")
        Servo_Angle += 1
        my_servo.angle = Servo_Angle


    time.sleep(0.001)

    if touch_A2.value and Servo_Angle > 0:
        print("Touched A2!")
        Servo_Angle -= 1
        my_servo.angle = Servo_Angle

    time.sleep(0.001)