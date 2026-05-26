#!/usr/bin/env python3
"""Module that converts a numpy array to a pandas DataFrame."""
import pandas as pd
import string


def from_numpy(array):
    """Creates a pd.DataFrame from a np.ndarray."""
    columns = list(string.ascii_uppercase[:array.shape[1]])
    return pd.DataFrame(array, columns=columns)
