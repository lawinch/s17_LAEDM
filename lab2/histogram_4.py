"""
Method:         Histogram
Data Variables: 2 variables:  number of bins and data
Author:         Fattakhova Yulduz
"""

import matplotlib.pyplot as plt


def plot_hist(x_label, bins_):
    plt.hist(x=x_label, normed=True, bins=bins_)
