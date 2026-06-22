#!/usr/bin/env python3
"""Module to calculate sensitivity."""
import numpy as np


def sensitivity(confusion):
    """
    Calculates the sensitivity for each class in a confusion matrix.
    confusion: numpy.ndarray of shape (classes, classes)
    Returns: numpy.ndarray of shape (classes,) containing sensitivity
    """
    # Her satırın toplamı o sınıfa ait toplam gerçek veriyi verir
    # Diagonal elemanlar doğru tahmin edilenleri verir
    true_positives = np.diag(confusion)
    actual_positives = np.sum(confusion, axis=1)

    # Sensitivity = TP / (TP + FN) = TP / Total Actual Positives
    return true_positives / actual_positives
