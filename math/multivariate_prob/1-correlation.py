#!/usr/bin/env python3
"""
Multivariate Probability - Correlation
"""
import numpy as np


def correlation(C):
    """
    Calculates a correlation matrix.

    Parameters:
    - C: numpy.ndarray of shape (d, d) containing a covariance matrix

    Returns:
    - A numpy.ndarray of shape (d, d) containing the correlation matrix
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    # Diqonal elementlərin kökünü alırıq (Standart kənarlaşmalar)
    diag = np.diag(C)
    std_dev = np.sqrt(diag)

    # Ölçünü (d, 1) edirik ki, broadcasting düzgün işləsin
    std_dev = std_dev[:, np.newaxis]

    # Korrelyasiya matrisinin hesablanması: C / (std_dev * std_dev.T)
    corr = C / np.matmul(std_dev, std_dev.T)

    return corr
