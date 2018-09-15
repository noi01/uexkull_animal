from pybrain.rl.environments.environment import Environment
from scipy import zeros
import random

#Rasberry Pi imports
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

def Forward():
	GPIO.output(11, 0)
	GPIO.output(13, 1)

def Snooze():
	GPIO.output(11, 0)
	GPIO.output(13, 0)

#sensor_input = 1 #integer mock input

sensor_input = [0, 1]


class Env(Environment):
    """ Environment for RL walking robot """       

    # the number of action values the environment accepts - Forward / stay 
    indim = 2
    
    # the number of sensor values the environment produces - n x light sensors
    outdim = 2
    
    
    
    def getSensors(self):
        """ the currently visible state of the world (the observation may be stochastic - repeated calls returning different values) 
            :rtype: by default, this is assumed to be a numpy array of doubles
        """
        
        sensor_value = random.choice(sensor_input)
        print sensor_value 
        
        return [float(sensor_value),]
        
                    
    def performAction(self, action):
        """ perform an action on the world that changes it's internal state (maybe stochastically).
            :key action: an action that should be executed in the Environment. 
            :type action: by default, this is assumed to be a numpy array of doubles
        """
        print "Action performed: ", action
        if  action >= 1: #any number
            print "Walk"
            Forward()
            #print sensor_value 
        else:
            Snooze()
            print "Not Walk"
            #print sensor_value
        

    def reset(self):
        """ Most environments will implement this optional method that allows for reinitialization. 
        """
