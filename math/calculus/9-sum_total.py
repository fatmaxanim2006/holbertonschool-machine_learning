#!/usr/bin/env python3
"""Sum of squares module"""


def summation_i_squared(n):
    """Calculates the sum of i^2 from 1 to n without loops"""
    if not isinstance(n, int) or n < 1:
        return None
    return (n * (n + 1) * (2 * n + 1)) // 6
