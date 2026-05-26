#!/usr/bin/env python3
"""
Module to fill missing values in DataFrame.
"""
import pandas as pd


def fill(df):
    """
    Cleans and fills missing values in the DataFrame.
    """
    # 1. 'Weighted_Price' sütununu silirik
    df = df.drop(columns=['Weighted_Price'])

    # 2. 'Close' sütunundakı NaN dəyərləri əvvəlki dəyərlə doldururuq (ffill)
    df['Close'] = df['Close'].ffill()

    # 3. 'High', 'Low', 'Open' sütunlarını 'Close' ilə doldururuq
    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])
    df['Open'] = df['Open'].fillna(df['Close'])

    # 4. Həcmləri (Volume) 0 ilə doldururuq
    df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
    df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

    return df
