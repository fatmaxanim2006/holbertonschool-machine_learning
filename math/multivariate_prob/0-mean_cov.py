#!/usr/bin/env python3
"""
Kovariasiya və orta qiyməti hesablayan modul
"""
import numpy as np


def mean_cov(X):
    """
    Data setin mean və covariance matrisini hesablayır.
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    n, d = X.shape

    if n < 2:
        raise ValueError("X must contain multiple data points")

    # Mean hesablanması: shape (1, d) olmalıdır
    mean = np.mean(X, axis=0, keepdims=True)

    # X elementlərindən mean çıxılır (broadcasting)
    X_centered = X - mean

    # Covariance hesablanması: (d, d) ölçüsündə matrix
    cov = np.matmul(X_centered.T, X_centered) / (n - 1)

    return mean, cov
