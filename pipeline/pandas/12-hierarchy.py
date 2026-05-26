#!/usr/bin/env python3
"""Module to arrange hierarchy in DataFrame."""
import pandas as pd


def hierarchy(df1, df2):
    """Rearranges MultiIndex, filters by timestamp and sorts."""
    index = __import__('10-index').index

    # 1. Her iki dataframe'i indexle
    df1 = index(df1)
    df2 = index(df2)

    # 2. Belirtilen zaman aralığını (1417411980 - 1417417980) filtrele
    df1 = df1[(df1.index >= 1417411980) & (df1.index <= 1417417980)]
    df2 = df2[(df2.index >= 1417411980) & (df2.index <= 1417417980)]

    # 3. İki dataframe'i birleştir (keys ile)
    df = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])

    # 4. MultiIndex seviyelerini değiştir (Timestamp ilk seviye olsun)
    df = df.swaplevel(0, 1)

    # 5. Kronolojik sıraya göre diz
    df = df.sort_index()

    return df
