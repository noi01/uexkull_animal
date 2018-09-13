from pybrain.rl.environments.environment import Environment
from scipy import zeros
import random



#sensor_input = 15 #integer
#sensor_input = random.sample([1, 2, 3, 4, 5],  1)
#random.uniform(1, 10)

sensor_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]


class Env(Environment):
    """ Environment for RL walking robot """       

    # the number of action values the environment accepts - Forward / stay 
    indim = 2
    
    # the number of sensor values the environment produces - n x light sensors
    # 1 x light sensors
    outdim = 20
    
    
    
    def getSensors(self):
        """ the currently visible state of the world (the observation may be stochastic - repeated calls returning different values) 
            :rtype: by default, this is assumed to be a numpy array of doubles
        """
        
        #sensor_input = 
        
        sensor_value = random.choice(sensor_input)
        print sensor_value 
        
        #int(sensor_input)
        #int(raw_input("Enter the state of the flower: ")) - 1
        # get 4 sensor readings from sensors / here input the sensors loop
        return [float(sensor_value),]
        
                    
    def performAction(self, action):
        """ perform an action on the world that changes it's internal state (maybe stochastically).
            :key action: an action that should be executed in the Environment. 
            :type action: by default, this is assumed to be a numpy array of doubles
        """
        print "Action performed: ", action
        if  action >= 1: #any number
            print "Walk"
            #print sensor_value 
        else:
            print "Not Walk"
            #print sensor_value
        

    def reset(self):
        """ Most environments will implement this optional method that allows for reinitialization. 
        """
