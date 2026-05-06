#!/usr/bin/env python3
"""Determinant hesablayan modul"""


def determinant(matrix):
    """
    Matrisin determinantını hesablayır.
    
    Args:
        matrix: Siyahılardan ibarət siyahı (list of lists).
        
    Returns:
        Matrisin determinantı.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    if matrix == [[]]:
        return 1
    
    n = len(matrix)
    if n == 0:
        return 1

    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a square matrix")

    # 1x1 matris üçün
    if n == 1:
        return matrix[0][0]

    # 2x2 matris üçün
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Daha böyük matrislər üçün rekursiv hesablama
    det = 0
    for c in range(n):
        # Minor matrisi yaratmaq
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(minor)
        
    return det
