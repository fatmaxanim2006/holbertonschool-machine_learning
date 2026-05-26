#!/usr/bin/env python3
"""
Module to sort and transpose a DataFrame.
"""


def flip_switch(df):
    """
    Sorts the data in reverse chronological order and transposes it.
    """
    # Timestamp üzrə tərsinə sıralayırıq və transponirə edirik (.T)
    return df.sort_values(by='Timestamp', ascending=False).T
