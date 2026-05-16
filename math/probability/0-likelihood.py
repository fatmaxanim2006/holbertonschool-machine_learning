#!/usr/bin/env python3
"""Ehtimal oxşarlığını (Likelihood) hesablayan modul."""
import numpy as np


def likelihood(x, n, P):
    """Binomial paylanmaya əsasən məlumatların likelihood massivini tapır."""
    if not isinstance(n, (int, np.integer)) or n <= 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(x, (int, np.integer)) or x < 0:
        msg = "x must be an integer that is greater than or equal to 0"
        raise ValueError(msg)

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")

    # Kombinasiya (n! / (x! * (n - x)!)) hesabı
    fact_n = np.math.factorial(n)
    fact_x = np.math.factorial(x)
    fact_nx = np.math.factorial(n - x)
    comb = fact_n / (fact_x * fact_nx)

    # Bütün P massivi üçün element-by-element Likelihood hesablanması
    # L = C(n, x) * P^x * (1 - P)^(n - x)
    like_val = comb * (P ** x) * ((1 - P) ** (n - x))

    return like_val
