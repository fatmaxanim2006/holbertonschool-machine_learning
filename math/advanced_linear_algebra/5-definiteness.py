#!/usr/bin/env python3
"""Matrisin definiteness növünü təyin edən modul"""
import numpy as np


def definiteness(matrix):
    """
    Matrisin definiteness növünü hesablayır.
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if len(matrix.shape) != 2 or \
       matrix.shape[0] != matrix.shape[1]:
        return None

    if not np.allclose(matrix, matrix.T):
        return None

    try:
        eigenvalues = np.linalg.eigvals(matrix)

        pos = np.all(eigenvalues > 0)
        pos_semi = np.all(eigenvalues >= 0)
        neg = np.all(eigenvalues < 0)
        neg_semi = np.all(eigenvalues <= 0)

        if pos:
            return "Positive definite"
        if neg:
            return "Negative definite"
        if pos_semi:
            return "Positive semi-definite"
        if neg_semi:
            return "Negative semi-definite"

        if any(eigenvalues > 0) and any(eigenvalues < 0):
            return "Indefinite"

        return None

    except Exception:
        return None
