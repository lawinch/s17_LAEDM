"""
Method:         Histogram
Data Variables: Random
Author:         Arthur Korochansky
"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

np.random.seed(0)
x_multi = [np.random.randn(n) for n in [100, 500, 50, 344]]

plt.hist(x_multi, 5, normed=1, histtype='bar', alpha=0.8)
plt.show()
