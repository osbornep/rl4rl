# Classroom Example

## Part 1 - Define Env

The first part defined the environment and creates the simulation. 

The output is a function that produces the outcome and reward signal of actions given the current state. This is then produced into the env.py file that can be imported into later sections.

## Part 2 - Model Based Policy Iteration

Given we have access to the model via the simulation, we show how Policy Iteration can be applied. We show only 1 policy update and the effect of this as a basic introduction to model-based methods.

## Part 3 - Online model Free Q Learning

We now assume the agent has no access to the underlying model, as it normal, and apply a model-free method of Q learning. The agent learns via episodes by interacting directly with the simulation. 

## Part 4 - Batch Offline Learning

Lastly, we show the learning process if we assume that the environment cannot be interacted with constantly. Instead, data must be collected and learned from offline in batches. We show how the observed probabilities differ from the true probablities which happen to be known to us given we built the simulation and the challenge of large data requirements. 


## Introducing the Environment

We formalise the problem into an example classroom with rows of students and a teacher.

The teacher is the controller of the system and would like for the paper to be passed to him/her and placed into the recycling bin, not the general trash. More formally:

- the paper should be passed along the class,
- in as few steps as possible,
- until it can be passed to the lecturer (controller) and will be placed in the bin.

We first show this as a real diagram and then how this can be formalised into a 'Grid World' example. In this example, students A and M are 'risky' individuals in that there is a chance that they attempt to throw the paper. As before, each student may pass or hold onto the paper (denoted by actions that go into a wall).

### Formalising the MDP

The MDP for the environment is deﬁned by:

- States are the students, teacher and the bin with 2-d(x,y) positions in the classroom
- Actions are commands given to each state and are deﬁned by [up, down, left, right]
- The transition probability function is deﬁned by the probability each state object has for successfully following the given action.
- The reward function is simply deﬁned as +1 for reaching the positive goal, -1 for reaching the negative goal and a small negative reward (e.g. -0.04) otherwise to encourage decisions that lead to the positive goal

The probabilities are defined by:

- The next state will depend on the current [x,y] state, action and probability distribution. If a “wall” is hit (e.g. C := [2,1] and action “up”) then the next state will remain the same as the current state.
- The teacher will always follow their command.
- Other students have the probability of following the action set to 0.8 and 0.1 for every other action
- The episode ends when the paper reaches the bin.



TODO: UPDATE IMAGES WITH TRASH/RECYCLING AS GOALS

![Classroom_real](https://i.imgur.com/nOIUKlg.png "Classroom in Real-World")

![Classroom_grid](https://i.imgur.com/WeJnqs2.png "Classroom as Grid-World")



