#!/usr/bin/env python3
"""
Module to slice DataFrame columns and rows.
"""


def slice(df):
    """
    Extracts specific columns and selects every 60th row.
    """
    # Sütunları seçirik və .iloc vasitəsilə hər 60-cı sətiri götürürük
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]
