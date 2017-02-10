"""
Method:         Dot plot
Data Variables: Y quantitative
X sequence
Author:         Mo Haoran
"""

import numpy as np
import matplotlib.pyplot as plt

Y = np.random.normal(0, 1, 1000)
X = np.linspace(0, 1000, 1000)
T = X
plt.scatter(X, Y, c=T)
plt.show()
