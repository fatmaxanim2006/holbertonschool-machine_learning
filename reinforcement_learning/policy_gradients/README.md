# Policy Gradients

This project covers Policy Gradient methods in reinforcement learning,
including computing a softmax policy, the Monte-Carlo policy gradient
algorithm (REINFORCE), and training an agent using policy gradients.

## Tasks

### 0. Simple Policy function
File: `policy_gradient.py`

Function `policy(matrix, weight)` computes the policy with a weight
of a matrix.

- `matrix`: `numpy.ndarray` containing the state
- `weight`: `numpy.ndarray` containing the weight
- Returns: the policy (action probabilities), computed via softmax
  of the dot product of `matrix` and `weight`

### Requirements
- Ubuntu 20.04 LTS, Python 3.9
- numpy

### Author
fatmaxanim2006
