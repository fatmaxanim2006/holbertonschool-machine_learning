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
    - mean: numpy.ndarray of shape (1, d) containing the mean of the data set
    - cov: numpy.ndarray of shape (d, d) containing the covariance matrix
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    n, d = X.shape

    if n < 2:
        raise ValueError("X must contain multiple data points")

    # Ortalama dəyərin hesarlanması: shape (1, d) olmalıdır
    mean = np.mean(X, axis=0, keepdims=True)

    # Məlumat nöqtələrindən ortalama çıxılır (Centering the data)
    X_centered = X - mean

    # Kovariasiya matrisinin numpy.cov olmadan hesarlanması: shape (d, d)
    # (n - 1) -ə bölünməsinin səbəbi unbiased estimator (nümunə kovariasiyası) olmasıdır
    cov = np.matmul(X_centered.T, X_centered) / (n - 1)

    return mean, cov
