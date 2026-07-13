#!/usr/bin/env python3
""" Gradient Descent with L2 Regularization """
import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """
    Updates the weights and biases of a neural network using gradient descent
    with L2 regularization.
    """
    m = Y.shape[1]
    
    # dz represents the derivative of the loss with respect to Z
    # Start with the last layer (Softmax activation)
    dz = cache[f'A{L}'] - Y
    
    # Iterate backwards from layer L to 1
    for i in range(L, 0, -1):
        A_prev = cache[f'A{i-1}']
        W = weights[f'W{i}']
        b = weights[f'b{i}']
        
        # Calculate gradients for weights and bias
        dw = (1 / m) * np.matmul(dz, A_prev.T) + (lambtha / m) * W
        db = (1 / m) * np.sum(dz, axis=1, keepdims=True)
        
        # Calculate dZ for the next iteration (previous layer)
        if i > 1:
            # Derivative of tanh is (1 - tanh^2)
            # A_prev is the output of the layer, already tanh applied
            dz = np.matmul(W.T, dz) * (1 - (A_prev ** 2))
            
        # Update weights and biases in place
        weights[f'W{i}'] -= alpha * dw
        weights[f'b{i}'] -= alpha * db
