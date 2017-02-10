"""
Method:         Scatter plot
Data Variables: 2 x quantitative
Author:         Maxim Skryabin
"""

import matplotlib.pyplot as plt


def plot_scatter(x, y, ax=plt.scatter(x, y, *xlabel=


    None, ylabel = None, ** kwargs):
*kwargs)
if xlabel:
    ax.set_xlabel(xlabel)
if ylabel:
    ax.set_ylabel(ylabel)
return ax

plot_scatter([1, 2], [2, 3])
plt.show()
