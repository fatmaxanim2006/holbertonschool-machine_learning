#!/usr/bin/env python3
"""Matrisin transpozisiyasını hesablayan funksiya"""


def matrix_transpose(matrix):
    """2D matrisin transpozisiyasını qaytarır"""
    return [[matrix[i][j] for i in range(len(matrix))]
            for j in range(len(matrix[0]))]
