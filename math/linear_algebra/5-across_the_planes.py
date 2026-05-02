#!/usr/bin/env python3
"""İki 2D matrisi element-element toplayan funksiya"""


def add_matrices2D(mat1, mat2):
    """İki matrisi toplayır, ölçülər fərqlidirsə None qaytarır"""
    # Sətir saylarını yoxla
    if len(mat1) != len(mat2):
        return None
    
    # Sütun saylarını yoxla (hər iki matrisin ilk sətirinə baxaraq)
    if len(mat1[0]) != len(mat2[0]):
        return None
    
    # Yeni matris yarat və cəmlə
    new_matrix = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])
        new_matrix.append(row)
        
    return new_matrix
