#!/usr/bin/env python3
"""Element-wise riyazi əməliyyatları yerinə yetirən funksiya"""


def np_elementwise(mat1, mat2):
    """Cəm, fərq, hasil və nisbəti tuple olaraq qaytarır"""
    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2
    return (add, sub, mul, div)
