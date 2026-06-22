#!/usr/bin/env python3
"""Module to calculate F1 score."""
import numpy as np


def f1_score(confusion):
    """
    Calculates the F1 score for each class in a confusion matrix.
    confusion: numpy.ndarray of shape (classes, classes)
    Returns: numpy.ndarray of shape (classes,) containing the F1 score
    """
    # Önceden yazılmış fonksiyonları içe aktarıyoruz
    sensitivity = __import__('1-sensitivity').sensitivity
    precision = __import__('2-precision').precision

    s = sensitivity(confusion)
    p = precision(confusion)

    # F1 score formülü
    return 2 * (p * s) / (p + s)
