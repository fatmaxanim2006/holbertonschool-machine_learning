#!/usr/bin/env python3
"""Computes the policy with a weight of a matrix"""
import numpy as np


def policy(matrix, weight):
    """
    Computes the policy with a weight of a matrix

    matrix: numpy.ndarray containing the state
    weight: numpy.ndarray containing the weight

    Returns: the policy (action probabilities)
    """
    z = matrix.dot(weight)
    exp = np.exp(z - np.max(z))
    return exp / np.sum(exp, axis=1, keepdims=True)
