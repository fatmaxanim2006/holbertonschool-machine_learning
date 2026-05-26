#!/usr/bin/env python3
"""Module that converts a numpy array to a pandas DataFrame."""
import pandas as pd


def from_numpy(array):
    """Creates a pd.DataFrame from a np.ndarray."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    columns = list(alphabet[:array.shape[1]])
    return pd.DataFrame(array, columns=columns)
