#!/usr/bin/env python3
"""Matrisin ölçüsünü hesablayan funksiya"""


def matrix_shape(matrix):
    """Matrisin ölçüsünü tam ədədlər siyahısı kimi qaytarır"""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
