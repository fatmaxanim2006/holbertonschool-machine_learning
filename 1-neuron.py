#!/usr/bin/env python3
"""
Defines a single neuron for binary classification with private attributes.
"""
import numpy as np


class Neuron:
    """
    Defines a single neuron performing binary classification.
    """
    def __init__(self, nx):
        """
        Initializes the neuron.
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        # Private instance attributes
        self.__W = np.random.normal(size=(1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Getter for the weights vector"""
        return self.__W

    @property
    def b(self):
        """Getter for the bias"""
        return self.__b

    @property
    def A(self):
        """Getter for the activated output"""
        return self.__A
