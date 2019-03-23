from pybrain.rl.environments.environment import Environment
from scipy import zeros
import random

#Rasberry Pi imports
import RPi.GPIO as GPIO
import time

#SETUP OUTPUT

GPIO.setmode(GPIO.BOARD)

# DC motors

GPIO.setup(15, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

def Forward():
    GPIO.output(15, 0)
    GPIO.output(13, 1)

def Backward():
    GPIO.output(15, 1)
    GPIO.output(13, 0)

def Snooze():
    GPIO.output(15, 0)
    GPIO.output(13, 0)
    


#SETUP INPUT

#define the sensor pins that goes to the circuit
photoresistor_sensor = 7
pir_sensor = 11

#analog sensor to digital input pin 
def rc_time(photoresistor_sensor):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(photoresistor_sensor, GPIO.OUT)
    GPIO.output(photoresistor_sensor, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(photoresistor_sensor, GPIO.IN)
  
    #Count until the pin goes high and cap the number at 1023
    while (GPIO.input(photoresistor_sensor) == GPIO.LOW and count<1023):
        count += 1

    return count
    
#digital sensor to digital input pin
def PIR_sensing (pir_sensor):
    
    GPIO.setup(pir_sensor, GPIO.IN)
    current_state = 0

    time.sleep(0.1)
    current_state = GPIO.input(pir_sensor)
    
    #return 1 or 0 
    if current_state == 1:
       return 1 

    elif current_state == 0:
        return 0



class Env(Environment):
    """ Environment for RL our agent will be able to observe"""       

    # the number of action values the environment accepts - Foreward, Backward and Snooze
    indim = 3
    
    # the number of sensor values the environment produces - analog in photoresistor_sensor
    outdim = 1024
    
    
    
    def getSensors(self):
        """ the currently visible state of the world (the observation may be stochastic - repeated calls returning different values) 
            :rtype: by default, this is assumed to be a numpy array of doubles
        """
        
        sensor_value = rc_time(photoresistor_sensor) #sensor messurment
# return needs to be formated in such way to be digestable by Pybrain library, I think... otherwise there are errors
        return [float(sensor_value),]
        
                    
    def performAction(self, action):
        """ perform an action on the world that changes it's internal state (maybe stochastically).
            :key action: an action that should be executed in the Environment. 
            :type action: by default, this is assumed to be a numpy array of doubles
        """
        print ("Action performed: ", action)
        if  action == 1:

            print ("I Walk")
            Forward()
            time.sleep(1)

        elif action == 2:
            print ("I Retreat")

            Backward()
            time.sleep(1)
            
        else:
            Snooze()
            print ("I don't walk")
            time.sleep(1)

        

    def reset(self):
        """ Most environments will implement this optional method that allows for reinitialization. 
        """
