#!/usr/bin/env python3
"""
Bayesian Probability - Intersection module
"""
import numpy as np


def intersection(x, n, P, Pr):
    """
    Calculates the intersection of obtaining this data with the various
    hypothetical probabilities.

    x: number of patients that develop severe side effects
    n: total number of patients observed
    P: 1D numpy.ndarray containing the various hypothetical probabilities
    Pr: 1D numpy.ndarray containing the prior beliefs of P
    """
    if not isinstance(n, (int, np.integer)) or n <= 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(x, (int, np.integer)) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
        )

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    # Pr obyektinin P ilə eyni ölçülü numpy massivi olmasını yoxlayırıq
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")

    # P massivindəki dəyərlərin [0, 1] aralığında olmasını yoxlayırıq
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")

    # Pr massivindəki dəyərlərin [0, 1] aralığında olmasını yoxlayırıq
    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")

    # Pr massivinin cəminin 1-ə bərabər olmasını np.isclose ilə yoxlayırıq
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    # Likelihood hesablanması (Binomial)
    fact_n = np.math.factorial(n)
    fact_x = np.math.factorial(x)
    fact_nx = np.math.factorial(n - x)
    combination = fact_n / (fact_x * fact_nx)

    likelihood = combination * (P ** x) * ((1 - P) ** (n - x))

    # Intersection = Likelihood * Prior
    return likelihood * Pr
