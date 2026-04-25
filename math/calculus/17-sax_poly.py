#!/usr/bin/env python3
"""Polynomial integral module"""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial"""
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    for x in poly:
        if not isinstance(x, (int, float)):
            return None

    if not isinstance(C, (int, float)):
        return None

    integral = [C]
    for i in range(len(poly)):
        # İnteqral qaydası: (əmsal / (qüvvət + 1))
        val = poly[i] / (i + 1)
        # Əgər nəticə tam ədəddirsə, int tipinə çeviririk
        if val % 1 == 0:
            val = int(val)
        integral.append(val)

    return integral
