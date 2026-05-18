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

        Parameters:
        - data: numpy.ndarray of shape (d, n) containing the data set
        """
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        # Calculate mean with shape (d, 1)
        self.mean = np.mean(data, axis=1, keepdims=True)

        # Center the data points
        data_centered = data - self.mean

        # Calculate covariance matrix with shape (d, d)
        self.cov = np.matmul(data_centered, data_centered.T) / (n - 1)

    def pdf(self, x):
        """
        Calculates the PDF at a data point

        Parameters:
        - x: numpy.ndarray of shape (d, 1) containing the data point

        Returns:
        - The value of the PDF
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.mean.shape[0]

        if len(x.shape) != 2 or x.shape[1] != 1 or x.shape[0] != d:
            raise ValueError("x must have the shape ({}, 1)".format(d))

        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)

        # Exponent hissəsinin hesablanması: -0.5 * (x - mu).T * inv * (x - mu)
        diff = x - self.mean
        exponent = -0.5 * np.matmul(np.matmul(diff.T, inv), diff)

        # Məxrəc hissəsi: sqrt((2 * pi)^d * det)
        denominator = np.sqrt(((2 * np.pi) ** d) * det)

        # PDF dəyəri matris formasında (1, 1) olacağı üçün skalyar olaraq çıxarırıq
        pdf_val = np.exp(exponent) / denominator

        return pdf_val[0, 0]
