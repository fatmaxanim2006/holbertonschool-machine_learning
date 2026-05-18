#!/usr/bin/env python3
"""
Multivariate Probability - Mean and Covariance
"""
import numpy as np


def mean_cov(X):
    """
    Calculates the mean and covariance of a data set.

    Parameters:
    - X: numpy.ndarray of shape (n, d) containing the data set

    Returns:
    - mean: numpy.ndarray of shape (1, d) containing the mean
    - cov: numpy.ndarray of shape (d, d) containing the covariance matrix
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    n, d = X.shape

    if n < 2:
        raise ValueError("X must contain multiple data points")

    # Calculate mean with shape (1, d)
    mean = np.mean(X, axis=0, keepdims=True)

    # Center the data points
    X_centered = X - mean

    # Calculate covariance matrix with shape (d, d)
    cov = np.matmul(X_centered.T, X_centered) / (n - 1)

    return mean, cov
