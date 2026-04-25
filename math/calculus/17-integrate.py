#!/usr/bin/env python3
"""
Defines a function that calculates the integral of a polynomial
"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial
    Args:
        poly: list of coefficients representing a polynomial
        C: integer representing the integration constant
    Returns:
        A new list of coefficients representing the integral, or None
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not all(isinstance(coef, (int, float)) for coef in poly):
        return None
    if not isinstance(C, int):
        return None

    # Integral of a_n * x^n is (a_n / (n + 1)) * x^(n + 1)
    integral = [C]
    for power, coef in enumerate(poly):
        new_coef = coef / (power + 1)
        # Represent as integer if it's a whole number
        if new_coef % 1 == 0:
            new_coef = int(new_coef)
        integral.append(new_coef)

    # Ensure the list is as small as possible (remove trailing zeros)
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
