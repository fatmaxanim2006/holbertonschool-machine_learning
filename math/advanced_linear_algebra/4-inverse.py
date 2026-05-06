#!/usr/bin/env python3
"""Matrisin tərsini hesablayan modul"""


def determinant(matrix):
    """Matrisin determinantını hesablayan köməkçi funksiya"""
    if matrix == [[]]:
        return 1
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(n):
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(minor)
    return det


def inverse(matrix):
    """
    Matrisin tərs matrisini (inverse) hesablayır.
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not matrix or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    det = determinant(matrix)

    # Əgər determinant 0-dırsa, matris singulardır (tərsi yoxdur)
    if det == 0:
        return None

    # 1x1 matris üçün tərs matris 1/element olur
    if n == 1:
        return [[1 / matrix[0][0]]]

    # Adjugate matrisini hesablayırıq
    cofactor_matrix = []
    for i in range(n):
        row_cofactors = []
        for j in range(n):
            sub_matrix = [row[:j] + row[j+1:] for row in
                          (matrix[:i] + matrix[i+1:])]
            cofactor_val = ((-1) ** (i + j)) * determinant(sub_matrix)
            row_cofactors.append(cofactor_val)
        cofactor_matrix.append(row_cofactors)

    # Transponirə edirik və hər bir elementi determinanta bölürük
    inv_matrix = []
    for j in range(n):
        new_row = []
        for i in range(n):
            new_row.append(cofactor_matrix[i][j] / det)
        inv_matrix.append(new_row)

    return inv_matrix
