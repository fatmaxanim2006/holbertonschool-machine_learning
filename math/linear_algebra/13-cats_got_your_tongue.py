#!/usr/bin/env python3
"""İki matrisi müəyyən ox üzrə birləşdirən funksiya"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Matrisləri verilmiş axis üzrə concatenate edir"""
    return np.concatenate((mat1, mat2), axis=axis)
