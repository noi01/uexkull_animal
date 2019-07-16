import RPi.GPIO as GPIO
import time
from time import sleep

# Part of Uexkull Animal code explanation

GPIO.setmode(GPIO.BCM)

# DC motors PIN Setup

GPIO.setup(15, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# Servo PIN Setup
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


# DC motors movement
def DC_Forward():
    GPIO.output(22, 0)
    GPIO.output(27, 1)

def DC_Backward():
    GPIO.output(22, 1)
    GPIO.output(27, 0)

def DC_Snooze():
    GPIO.output(22, 0)
    GPIO.output(27, 0)
	

# Servo motors movement
def Servo_Forward():
    kit.servo[0].angle = 90
    kit.servo[1].angle = 90
    sleep(1)
	kit.servo[0].angle = 140
    kit.servo[1].angle = 140
    sleep(1)
	kit.servo[0].angle = 0
    kit.servo[1].angle = 0
    sleep(1)

    
def Servo_Snooze():
    kit.servo[0].angle = 90
    kit.servo[1].angle = 90
    sleep(1)
    
# DC motors loop - loops 5 times
for x in range(6):
    DC_Forward()
    sleep(1)
    DC_Backward()
    sleep(1)
    DC_Snooze()

# Servo motors loop - loops 5 times
for x in range(6):
    Servo_Forward()
    Servo_Snooze()
