#!/usr/bin/env python3
"""Module to plot a stacked bar graph."""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """Plots a stacked bar graph of fruit per person."""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    # İnsan adları və meyvə rəngləri
    people = ['Farrah', 'Fred', 'Felicia']
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
    fruits = ['apples', 'bananas', 'oranges', 'peaches']

    # Yığınlı sütunları yaratmaq
    bottom = np.zeros(3)
    for i in range(len(fruit)):
        plt.bar(people, fruit[i], width=0.5, bottom=bottom,
                color=colors[i], label=fruits[i])
        bottom += fruit[i]

    # Qrafikin tənzimlənməsi
    plt.ylabel('Quantity of Fruit')
    plt.title('Number of Fruit per Person')
    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10))
    plt.legend()

    plt.show()
