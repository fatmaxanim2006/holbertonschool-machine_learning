#!/usr/bin/env python3
"""
Module to sort DataFrame by High price.
"""


def high(df):
    """
    Sorts the DataFrame by the 'High' column in descending order.
    """
    # 'High' sütununa görə azalan sırada (ascending=False) sıralayırıq
    return df.sort_values(by='High', ascending=False)
