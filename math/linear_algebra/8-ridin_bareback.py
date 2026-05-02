#!/usr/bin/env python3
"""Matrislərin vurulmasını həyata keçirən funksiya"""


def mat_mul(mat1, mat2):
    """İki matrisi vurur, mümkün deyilsə None qaytarır"""
    # Matris vurulması şərti: mat1-in sütun sayı == mat2-nin sətir sayı
    if len(mat1[0]) != len(mat2):
        return None

    # Nəticə matrisinin ölçüləri: len(mat1) x len(mat2[0])
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            # Skalyar hasil (dot product) hesablama
            element = 0
            for k in range(len(mat2)):
                element += mat1[i][k] * mat2[k][j]
            row.append(element)
        result.append(row)

    return result
