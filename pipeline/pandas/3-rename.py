#!/usr/bin/env python3
"""
Module to rename and convert columns in a DataFrame.
"""
import pandas as pd


def rename(df):
    """
    Renames the Timestamp column to Datetime, converts it to datetime objects,
    and returns a DataFrame with only Datetime and Close columns.
    """
    # Sütun ismini değiştirme
    df = df.rename(columns={'Timestamp': 'Datetime'})
    
    # Unix timestamp'i datetime formatına dönüştürme
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')
    
    # Sadece Datetime ve Close sütunlarını seçme
    df = df[['Datetime', 'Close']]
    
    return df
