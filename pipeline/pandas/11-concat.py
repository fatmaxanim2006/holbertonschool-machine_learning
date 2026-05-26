#!/usr/bin/env python3
"""Module to concatenate two DataFrames."""
import pandas as pd


def concat(df1, df2):
    """Concatenates two DataFrames with specific indexing and keys."""
    index = __import__('10-index').index

    # Indexleme işlemini 10-index modülünü kullanarak yapın
    df1 = index(df1)
    df2 = index(df2)

    # df2'yi 1417411920 timestamp'ine kadar filtrele
    df2 = df2[df2.index <= 1417411920]

    # İki dataframe'i birleştir (df2 üstte, df1 altta)
    df = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])

    return df
