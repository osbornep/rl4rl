# Robot Cleaner Example

## Introducing the Environment

The environment's probabilities are calcualted based on the direction in which the paper is thrown and the current distance from the bin. 

For example, in the image below we have three people labelled A, B and C. A and B both throw in the correct direction but person A is closer than B and so will have a higher probability of landing the shot. 

Person C is closer than person B but throws in the completely wrong direction and so will have a very low probability of hitting the bin. This may seem illogical that person C would throw in this direction but, as we will show more later, an algorithm has to try a range of directions first to figure out where the successes are and will have no visual guide as to where the bin is. 

![Enironment Demo](https://i.imgur.com/3woVbKI.png)



## Part 1 Applying RL Naively

In this first part, we are provided with a function that captures the environment and use this to naiively apply Q-learning without any further understanding of the model.

## Part 2 Define Env

Following part 1, we evaluate where the function comes from and show how this can be defined in the simulation.

## Part 3 Applying Value Iteration

Given we have access to the model from part 2, we apply a dynamic programming approach to find the optimal policy.

## Part 4 Applying Q-Learning

Lastly, we reintroduce Q-learning to solve the environment and apply more complex parameter selection.


