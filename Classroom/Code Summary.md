# Code Summary (Python)

Script Files:

1. Q_learning_fn.py
2. env.py
3. run.py



### Q_learning_fn.py

Defines a simple Q learning agent.

Inputs: 

1. Environment: 
  - states - list of state names
  - actions - possible actions
  - rewards - reward function values
  - [x_list, y_list] - x,y position of states
  - Q_table - initialised Q values
  - start_state - specific start state if needed
2. Parameters: 
  - num_episodes - Number of episodes  
  - epsilon - Epsilon-greedy parameter
  - num_random_episodes - Fixed number of episodes to explore at start
  - alpha - Learning Rate parameter
  - gamma - Discount Rate parameter

