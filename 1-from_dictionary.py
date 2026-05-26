#!/usr/bin/env python3
"""Module that creates a pd.DataFrame from a dictionary."""
import pandas as pd

# Lüğəti yaradırıq
data = {
    'First': [0.0, 0.5, 1.0, 1.5],
    'Second': ['one', 'two', 'three', 'four']
}

# DataFrame-i yaradırıq və indeksləri təyin edirik
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])
