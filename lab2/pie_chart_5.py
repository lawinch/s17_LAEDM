"""
Method:         Pie chart
Data Variables: labels - strings

sizes - quantitative
Author:         Vladimir Shevchenko
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_pie(labels, sizes):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    return plt


# data
n = 5
max_value = 1000
labels = ['Label ' + str(i) for i in range(n)]
sizes = np.random.randint(0, max_value, n)

plot = plot_pie(labels, sizes)
plot.show()
