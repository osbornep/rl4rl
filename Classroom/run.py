# Default Imports
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import figure

import tqdm
import time

import warnings
warnings.filterwarnings("ignore")

# Import environment from env.py
from env import action_outcome
from env import environment

# Import Q Learning function from Q_learning_fn.py
from Q_learning_fn import Q_learning

# Figure Formatting
sns.set(rc={'figure.figsize':(15, 10)})
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 5})

sns.set_style("whitegrid", {'axes.grid' : False})

#------------------------------------------------------------------------------------------
# ENVIRONMENT REQUIREMENTS
## Define states with 1) Labels, 2) Rewards and 3) [x,y] coordinates
states = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T', 'M', 'recycling', 'trash']
rewards = [-0.04, -0.04, -0.04, -0.04, -0.04, -0.04, -0.04, -0.04, -0.04, 1, -1]
x_list = [4,3,2,1,1,1,2,3,3,4,4]
y_list = [1,1,1,1,2,3,3,3,2,3,2]

## The low-level actions the agent can make in the environment
actions = ['left','right','up','down']

#------------------------------------------------------------------------------------------
# Initialise RL agent

## Fix episode start if running on small scale for understanding
start_state = None

## Parameters
num_episodes = 500
epsilon = 0.2
num_random_episodes = 50
alpha = 0.2
gamma = 0.8

## Initialise Q Values equal to 0
Q_table = pd.DataFrame()
for n1,state in enumerate(states):
    action_list = pd.DataFrame()
    for n2,action in enumerate(actions):
        state_x = x_list[n1]
        state_y = y_list[n1]
        u = action_outcome(state_x,state_y,action)[0]
        v = action_outcome(state_x,state_y,action)[1]
        action_list  = action_list.append(pd.DataFrame({'state':state,'x':x_list[n1],'y':y_list[n1],'u':u,'v':v, 'action':action}, index=[(n1*len(actions)) + n2]))

    Q_table = Q_table.append(action_list)
Q_table['Q']=0

print(Q_table.head())

#------------------------------------------------------------------------------------------
# Apply Q Learning Agent

Mdl = Q_learning_v1(Q_table, start_state, num_episodes, epsilon, num_random_episodes, alpha, gamma)
Q_table_output = Mdl[0]
Q_table_tracker_output = Mdl[1]

plt.plot(Q_table_tracker_output['total_Q'])
plt.ylabel("Total Q")
plt.xlabel("Episode")
plt.title("Total Q by Episode")
plt.show()

# Normalise so we can still plot negative values
Q_table_output['Q_norm'] = (Q_table_output['Q']-min(Q_table_output['Q']))/( max(Q_table_output['Q']) - min(Q_table_output['Q']) )
Q_table_output.head(50)

# Plot best actions in each state
for n,state in enumerate(states):
    if state == 'recycling':
        plt.scatter(x_list[n],y_list[n], s=150, color='g', marker='+')
    elif state == 'trash':
        plt.scatter(x_list[n],y_list[n], s=150, color='r', marker='x')
    else:
        plt.scatter(x_list[n],y_list[n], s=150, color='b')
    plt.text(x_list[n]+0.05,y_list[n]+0.05,states[n])
    Q_table_output_state = Q_table_output[Q_table_output['state']==state].reset_index(drop=True)
    for action in range(0,len(Q_table_output_state)):
        if (Q_table_output_state['Q_norm'].iloc[action] == Q_table_output_state['Q_norm'].max()):
            plt.quiver(x_list[n],y_list[n],Q_table_output_state['u'][action],Q_table_output_state['v'][action], alpha = 0.5,
                      width = 0.01*Q_table_output_state['Q_norm'][action])
    
plt.title("Grid World Diagram for Classroom Paper Throwing Environment: \n Optimal Action for each State")
plt.xticks([])
plt.yticks([])
plt.ylim(0,4)
plt.xlim(0,5)
plt.show()

