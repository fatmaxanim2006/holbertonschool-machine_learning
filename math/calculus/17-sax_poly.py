#!/usr/bin/env python3
"""Polynomial integral module"""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial"""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not isinstance(C, (int, float)):
        return None
    integral = [C]
    for i in range(len(poly)):
        if not isinstance(poly[i], (int, float)):
            return None
        val = poly[i] / (i + 1)
        integral.append(int(val) if val % 1 == 0 else val)
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    return integral
