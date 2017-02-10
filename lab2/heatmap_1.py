"""
Method:         Heatmap
Data Variables: Both Axes - Quantitative (random)
Author:         Kenneth Nwafor
"""

import numpy as np
import numpy.random
import matplotlib.pyplot as plt

x = np.random.randn(10873)
y = np.random.randn(10873)

heatmap, xedges, yedges = np.histogram2d(x, y, bins=70)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plt.clf()
plt.imshow(heatmap.T, extent=extent, origin='lower')
plt.show()
