#!/usr/bin/env python3
"""İki siyahını element-element toplayan funksiya"""


def add_arrays(arr1, arr2):
    """İki siyahını toplayır, ölçülər fərqlidirsə None qaytarır"""
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
