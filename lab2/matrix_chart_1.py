"""
Method:         Matrix chart
Data Variables: quantitative
Author:         Marat Vinokurov
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_matrix(matrix):
    plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.ocean)
    plt.colorbar()
    plt.show()


m = np.random.rand(10, 10)
matrix = np.matrix(m)
plot_matrix(matrix)
