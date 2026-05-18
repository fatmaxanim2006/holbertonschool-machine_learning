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

        # Ortalamanın hesablanması: hər sətir üzrə, shape (d, 1) olmalıdır
        self.mean = np.mean(data, axis=1, keepdims=True)

        # Məlumat nöqtələrindən ortalama çıxılır (Centering data)
        data_centered = data - self.mean

        # Kovariasiya matrisinin hesablanması: shape (d, d)
        # data_centered ölçüsü (d, n) olduğu üçün özünü transpozisiyasına vururuq
        self.cov = np.matmul(data_centered, data_centered.T) / (n - 1)
