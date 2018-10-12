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

# define action-value table:
# number of environment states:
# 1024 states agent can be in the environment - comfortable / uncomfortable
#
# number of actions:
# 3 the number of action values the environment accepts -  Foreward, Backward and Snooze

states = 1024 #Has to match class Env(Environment) - outdim  in environment_01.py
actions = 3 #Has to match class Env(Environment) - indim  in environment_01.py

try:
    arr = np.loadtxt('/home/pi/Desktop/uexkull_animal/uexkull.csv', delimiter=';')
    # open action value table  from .csv file
except Exception as e:
    print e
    arr = np.zeros((states, actions))
    # except if the file does not exist - ie. first time - then creat and initialize it with numpy of zeros

av_table = ActionValueTable(states, actions)
av_table.initialize(arr.flatten())

# define Q-learning agent
learner = Q(0.1, 0.5)
learner._setExplorer(EpsilonGreedyExplorer(0.5))
agent = LearningAgent(av_table, learner)

# define the environment
env = Env()

# define the task
task = Task(env)

# define experiment
experiment = Experiment(task, agent)

# ready to go, start the process
while True:
    experiment.doInteractions(12)
    agent.learn()
    agent.reset()

    export_arr = av_table.getActionValues(np.arange(states))
    export_arr = export_arr.reshape((states, actions))

    np.savetxt("/home/pi/Desktop/uexkull_animal/uexkull.csv", export_arr, fmt='%.3f', delimiter=';')
    # save action value table to .csv file