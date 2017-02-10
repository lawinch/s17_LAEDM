"""
Method:         Bubble plot
Data Variables: 3 quantitative
Author:         Timur Kasatkin
"""

import matplotlib.pyplot as plt


def scatter_plot(x, y, r, xlabel=None, ylabel=None):
    ax = plt.scatter(x, y, r)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    return ax


scatter_plot([4, 3, 2, 1], [10, 11, 12, 13], [20, 40, 80, 170])
plt.show()
