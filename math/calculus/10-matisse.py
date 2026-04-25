#!/usr/bin/env python3
"""Polynomial derivative module"""


def poly_derivative(poly):
    """Calculates the derivative of a polynomial"""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    derivative = []
    for i in range(1, len(poly)):
        if not isinstance(poly[i], (int, float)):
            return None
        derivative.append(i * poly[i])
    while len(derivative) > 1 and derivative[-1] == 0:
        derivative.pop()
    return derivative
