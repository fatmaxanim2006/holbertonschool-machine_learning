#!/usr/bin/env python3
"""
Module to remove rows with NaN values in 'Close'.
"""


def prune(df):
    """
    Removes any entries where 'Close' has NaN values.
    """
    # subset='Close' ilə yalnız 'Close' sütununda NaN olanları sətir üzrə silirik
    return df.dropna(subset=['Close'])
