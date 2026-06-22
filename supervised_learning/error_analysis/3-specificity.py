#!/usr/bin/env python3
"""Module to calculate specificity."""
import numpy as np


def specificity(confusion):
    """
    Calculates the specificity for each class in a confusion matrix.
    confusion: numpy.ndarray of shape (classes, classes)
    Returns: numpy.ndarray of shape (classes,) containing the specificity
    """
    # Her sınıf için TP, FP, FN, TN hesaplayalım
    # TP: Diagonal elemanlar
    tp = np.diag(confusion)
    
    # FP: Sütun toplamları - TP
    fp = np.sum(confusion, axis=0) - tp
    
    # FN: Satır toplamları - TP
    fn = np.sum(confusion, axis=1) - tp
    
    # TN: Toplam - (TP + FP + FN)
    total = np.sum(confusion)
    tn = total - (tp + fp + fn)
    
    # Specificity = TN / (TN + FP)
    return tn / (tn + fp)
