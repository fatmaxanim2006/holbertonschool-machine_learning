#!/usr/bin/env python3
"""Neuron module"""
import numpy as np

class Neuron:
    """Defines a single neuron performing binary classification"""
    def __init__(self, nx):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
    <-- burada gizli boşluq var (12-ci sətir)
        self.nx = nx
        ...
