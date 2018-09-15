from task_01 import Task
from environment_01 import Env
from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import Q
from pybrain.rl.experiments import Experiment
from pybrain.rl.explorers import EpsilonGreedyExplorer

import pylab
import numpy as np

#Rasberry Pi imports
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# define action-value table
# number of states is:
#
#   2 states agent can be in the environment - comfortable / uncomfortable

# number of actions:
#
# 2 the number of action values the environment accepts -  walk/not walk

states = 2 #Has to match class Env(Environment) in Environment - outdim
actions = 2 #Has to match class Env(Environment) in Environment - indim 

try:
    arr = np.loadtxt('uexkull.csv', delimiter=';')
except Exception as e:
    print e
    arr = np.zeros((states, actions))

av_table = ActionValueTable(states, actions)
av_table.initialize(arr.flatten())

# define Q-learning agent
learner = Q(0.1, 0.5) #uncomment fo Q learning / comment 
learner._setExplorer(EpsilonGreedyExplorer(0.5)) #uncomment 
agent = LearningAgent(av_table, learner)

# define the environment
env = Env()

# define the task
task = Task(env)

# finally, define experiment
experiment = Experiment(task, agent)

# ready to go, start the process
while True:
    experiment.doInteractions(12)
    agent.learn()
    agent.reset()

    export_arr = av_table.getActionValues(np.arange(states))
    export_arr = export_arr.reshape((states, actions))

    np.savetxt("uexkull.csv", export_arr, fmt='%.3f', delimiter=';')
