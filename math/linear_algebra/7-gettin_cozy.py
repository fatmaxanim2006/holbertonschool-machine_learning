#!/usr/bin/env python3
"""Matrisləri ox üzrə birləşdirən funksiya"""


def cat_matrices2D(mat1, mat2, axis=0):
    """İki matrisi axis 0 və ya 1 üzrə birləşdirir"""
    if axis == 0:
        # Sütun sayı eyni olmalıdır
        if len(mat1[0]) != len(mat2[0]):
            return None
        # Orijinal elementləri kopyalayaraq yeni siyahı yaradırıq
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    if axis == 1:
        # Sətir sayı eyni olmalıdır
        if len(mat1) != len(mat2):
            return None
        # Hər sətiri birləşdirərək yeni sətirlər yaradırıq
        return [mat1[i] + mat2[i] for i in range(len(mat1))]

    return None
