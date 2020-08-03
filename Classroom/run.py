sns.set(rc={'figure.figsize':(15, 10)})
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 5})

sns.set_style("whitegrid", {'axes.grid' : False})

#------------------------------------------------------------------------------------------

# Define states with 1) Labels, 2) Rewards and 3) [x,y] coordinates
states = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T', 'M', 'recycling', 'trash']
rewards = [-0.04, -0.04, -0.04, -0.04, -0.04, -0.04, -0.04, -0.04, -0.04, 1, -1]
x_list = [4,3,2,1,1,1,2,3,3,4,4]
y_list = [1,1,1,1,2,3,3,3,2,3,2]

# The low-level actions the agent can make in the environment
actions = ['left','right','up','down']
