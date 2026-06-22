#!/usr/bin/env python3
"""Module to create a confusion matrix."""
import numpy as np


def create_confusion_matrix(labels, logits):
    """
    Creates a confusion matrix.
    labels: one-hot numpy.ndarray of shape (m, classes)
    logits: one-hot numpy.ndarray of shape (m, classes)
    Returns: a confusion numpy.ndarray of shape (classes, classes)
    """
    true_labels = np.argmax(labels, axis=1)
    predicted_labels = np.argmax(logits, axis=1)

    num_classes = labels.shape[1]

    confusion_matrix = np.zeros((num_classes, num_classes))

    for i in range(len(true_labels)):
        confusion_matrix[true_labels[i], predicted_labels[i]] += 1

    return confusion_matrix
