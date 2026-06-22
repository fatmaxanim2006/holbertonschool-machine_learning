#!/usr/bin/env python3
"""Module to calculate specificity."""
import numpy as np


def specificity(confusion):
    """
    Calculates the specificity for each class in a confusion matrix.
    confusion: numpy.ndarray of shape (classes, classes)
    Returns: numpy.ndarray of shape (classes,) containing the specificity
    """
    tp = np.diag(confusion)
    fp = np.sum(confusion, axis=0) - tp
    fn = np.sum(confusion, axis=1) - tp
    total = np.sum(confusion)
    tn = total - (tp + fp + fn)
    return tn / (tn + fp)
