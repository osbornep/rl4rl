# Classroom Example

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
