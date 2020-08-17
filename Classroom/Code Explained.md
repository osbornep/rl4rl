# Code Summary (Python)

Script Files:

1. Q_learning_fn.py
2. env.py
3. run.py



## Q_learning_fn.py

Defines a simple Q learning agent.

### Inputs: 

**Environment**: 
  - states - list of state names
  - actions - possible actions
  - rewards - reward function values
  - [x_list, y_list] - x,y position of states
  - Q_table - initialised Q values
  - start_state - specific start state if needed
  
**Parameters**: 
  - num_episodes - Number of episodes  
  - epsilon - Epsilon-greedy parameter
  - num_random_episodes - Fixed number of episodes to explore at start
  - alpha - Learning Rate parameter
  - gamma - Discount Rate parameter

### Summary

For the specific number of episodes, the agent takes actions until a terminal state is reached. Terminal states are 'trash' or 'recycling' and are fixed.

After each action, Q value is updated by:

![Q Learning Update Rule](https://i.imgur.com/nOpmUUz.png "Q-Learning Update Rule")
