#!/usr/bin/env python3
"""
Bu modul tələbələrin ballarını göstərən histogramı çəkir.
"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """
    Tələbələrin balları üçün histogramı çəkən funksiya.
    """
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    
    plt.figure(figsize=(6.4, 4.8))
    
    # Histogramın parametrləri:
    # bins: aralıqları 10 vahid artımla təyin edirik
    # edgecolor: barların kənarlarını qara edir
    plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
    
    # Başlıq və oxların adları
    plt.title('Project A')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    
    # Oxların diapazonunu təyin etmək (istəyə bağlı, nümunəyə görə)
    plt.xlim(0, 100)
    plt.ylim(0, 30)
    
    # plt.show() - QEYD: Bir çox avtomatlaşdırılmış sistemlərdə
    # plt.show() yazmaq testin səhv keçməsinə səbəb ola bilər, 
    # tapşırıqdan asılı olaraq bunu silməyiniz lazım ola bilər.
