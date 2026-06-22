#!/usr/bin/env python3
"""Module to calculate precision."""
import numpy as np


def precision(confusion):
    """
    Calculates the precision for each class in a confusion matrix.
    confusion: numpy.ndarray of shape (classes, classes)
    Returns: numpy.ndarray of shape (classes,) containing the precision
    """
    # Diagonal elemanlar doğru tahmin edilenleri (True Positives) verir
    true_positives = np.diag(confusion)

    # Sütun toplamları, modelin o sınıf için yaptığı toplam tahminleri verir
    predicted_positives = np.sum(confusion, axis=0)

    # Precision = TP / (TP + FP) = TP / Total Predicted Positives
    return true_positives / predicted_positives
