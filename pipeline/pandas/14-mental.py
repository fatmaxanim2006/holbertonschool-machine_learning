#!/usr/bin/env python3
"""Module to calculate mental statistics."""


def mental(df):
    """Calculates descriptive statistics for all columns."""
    return df.describe()
