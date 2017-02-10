"""
Method:         Line chart
Data Variables: quantitative
Author:         Marat Vinokurov
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_line(x, y):
    plt.plot(x, y)
    plt.show()


values = np.linspace(0, 100)
plot_line(values, np.cos(values))
