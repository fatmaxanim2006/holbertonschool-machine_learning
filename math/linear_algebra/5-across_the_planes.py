#!/usr/bin/env python3
"""İki 2D matrisi element-element toplayan funksiya"""


def add_matrices2D(mat1, mat2):
    """İki matrisi toplayır, ölçülər fərqlidirsə None qaytarır"""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    new_matrix = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])
        new_matrix.append(row)

    return new_matrix
