"""
Method:         Dot Plot
Data Variables: 2 x numbers
Author:         Dmitry Mordovtsev
"""

import numpy as np
import matplotlib.pyplot as plt


def dot_plot(x, y, colors, **kwargs):
    area = np.pi * 5
    ax = plt.scatter(x, y, s=area, c=colors, **kwargs)
    return ax


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
dot_plot(x, y, colors)
plt.show()
