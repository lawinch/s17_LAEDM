"""
Method:         Stacked area chart
Data Variables: x, y - quantitative
Author:         Vladimir Shevchenko
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_stacked_area(x, y):
   plt.stackplot(x, y)
   return plt

#data
n = 10
max_value = 1000
y_count = 5

x = np.arange(n)
y = np.random.randint(0, max_value, (y_count, n))

plot = plot_stacked_area(x, y)
plot.show()