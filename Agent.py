
from task_01 import Task
from environment_01 import Env
from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import Q
from pybrain.rl.experiments import Experiment
from pybrain.rl.explorers import EpsilonGreedyExplorer

import pylab
import numpy as np

# define action-value table
# number of states is:
#
#   2 states - comfortable / uncomfortable
#   2 actions - walk/not walk
# number of actions:
#
# 4 - the number of action values the environment accepts - Forward on rotation 0, 90, 180, 270 
states = 20
actions = 2

try:
    arr = np.loadtxt('av_table_aiy.csv', delimiter=';')
except Exception as e:
    print e
    arr = np.zeros((states, actions))

av_table = ActionValueTable(states, actions)
av_table.initialize(arr.flatten())

# define Q-learning agent
learner = Q(0.5, 0.0)
learner._setExplorer(EpsilonGreedyExplorer(0.0))
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

    np.savetxt("av_table_aiy.csv", export_arr, fmt='%.3f', delimiter=';')
