#!/usr/bin/env python3
"""
Module to plot a histogram of student grades
"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """
    Plots a histogram of student grades for Project A
    """
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # Histogramın yaradılması
    plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')

    # Etiketlər və başlıq
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')

    # X oxunun diapazonu
    plt.xlim(0, 100)
    plt.show()
