from pybrain.rl.environments.environment import Environment
from scipy import zeros
import random

#Rasberry Pi imports
import RPi.GPIO as GPIO
import time

#SETUP OUTPUT

GPIO.setmode(GPIO.BOARD)

# DC motors

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

def Forward():
	GPIO.output(11, 0)
	GPIO.output(13, 1)

def Backward():
	GPIO.output(11, 1)
	GPIO.output(13, 0)

def Snooze():
	GPIO.output(11, 0)
	GPIO.output(13, 0)
	
#SETUP INPUT

pin_to_circuit = 7 #define the sensor pin that goes to the circuit

#analog sensor to digital input pin
def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high and cap the number at 1023
    while (GPIO.input(pin_to_circuit) == GPIO.LOW and count<1023):
        count += 1

    return count
    

class Env(Environment):
    """ Environment for RL walking robot """       

    # the number of action values the environment accepts - Foreward, Backward and Snooze
    indim = 3
    
    # the number of sensor values the environment produces - analog in photoresistor
    outdim = 1024
    
    
    
    def getSensors(self):
        """ the currently visible state of the world (the observation may be stochastic - repeated calls returning different values) 
            :rtype: by default, this is assumed to be a numpy array of doubles
        """
        
        sensor_value = rc_time (pin_to_circuit) #sensor messurment
        
        return [float(sensor_value),]
        
                    
    def performAction(self, action):
        """ perform an action on the world that changes it's internal state (maybe stochastically).
            :key action: an action that should be executed in the Environment. 
            :type action: by default, this is assumed to be a numpy array of doubles
        """
        print "Action performed: ", action
        if  action == 1: 
            print "I Walk"
            Forward()
            time.sleep(1)

        elif action == 2:
            print "I Retreat"
            Backward()
            time.sleep(1)
            
        else:
            Snooze()
            print "I don't walk"
            time.sleep(1)

        

    def reset(self):
        """ Most environments will implement this optional method that allows for reinitialization. 
        """
