#!/usr/bin/env python3
"""Module to set index of DataFrame."""


def index(df):
    """Sets the Timestamp column as the index of the dataframe."""
    df = df.set_index('Timestamp')
    return df
