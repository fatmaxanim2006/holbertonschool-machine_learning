#!/usr/bin/env python3
"""
Multivariate Normal distribution class
"""
import numpy as np


class MultiNormal:
    """
    Represents a Multivariate Normal distribution
    """

    def __init__(self, data):
        """
        Class constructor
        """
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)
        data_centered = data - self.mean
        self.cov = np.matmul(data_centered, data_centered.T) / (n - 1)

    def pdf(self, x):
        """
        Calculates the PDF at a data point
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.mean.shape[0]

        if len(x.shape) != 2 or x.shape[1] != 1 or x.shape[0] != d:
            raise ValueError("x must have the shape ({}, 1)".format(d))

        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)

        diff = x - self.mean

        # Dəqiq skalyar dəyər almaq üçün matris hasilləri
        inv_diff = np.matmul(inv, diff)
        exponent = -0.5 * np.matmul(diff.T, inv_diff)

        denominator = np.sqrt(((2 * np.pi) ** d) * det)
        pdf_val = np.exp(exponent) / denominator

        return pdf_val[0, 0]
