#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def all_in_one():
    y0 = np.arange(0, 11) ** 3
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180
    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)
    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    fig = plt.figure(figsize=(10, 8))
    fig.suptitle('All in One', fontsize='x-small')
    gs = fig.add_gridspec(3, 2)

    # 1. Qrafik
    ax0 = fig.add_subplot(gs[0, 0])
    ax0.plot(np.arange(0, 11), y0, 'r-')
    ax0.set_xlim(0, 10)

    # 2. Qrafik
    ax1 = fig.add_subplot(gs[0, 1])
    ax1.scatter(x1, y1, color='magenta', s=10)
    ax1.set_title("Men's Height vs Weight", fontsize='x-small')
    ax1.set_xlabel('Height (in)', fontsize='x-small')
    ax1.set_ylabel('Weight (lbs)', fontsize='x-small')

    # 3. Qrafik
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.plot(x2, y2)
    ax2.set_title('Exponential Decay of C-14', fontsize='x-small')
    ax2.set_xlabel('Time (years)', fontsize='x-small')
    ax2.set_ylabel('Fraction Remaining', fontsize='x-small')
    ax2.set_yscale('log')

    # 4. Qrafik
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.plot(x3, y31, 'r--', label='C-14')
    ax3.plot(x3, y32, 'g-', label='Ra-226')
    ax3.set_title('Exponential Decay of Radioactive Elements', fontsize='x-small')
    ax3.set_xlabel('Time (years)', fontsize='x-small')
    ax3.set_ylabel('Fraction Remaining', fontsize='x-small')
    ax3.legend(fontsize='x-small')

    # 5. Qrafik (2 sütun genişliyində)
    ax4 = fig.add_subplot(gs[2, :])
    ax4.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
    ax4.set_title('Project A', fontsize='x-small')
    ax4.set_xlabel('Grades', fontsize='x-small')
    ax4.set_ylabel('Number of Students', fontsize='x-small')
    ax4.set_xlim(0, 100)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
