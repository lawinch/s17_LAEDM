"""
Method:         Heatmap
Data Variables: Random 
Author:         Rustam Tukhvatov
"""

import numpy as np
import numpy.random
import matplotlib.pyplot as plt


x = np.random.randn(8000)
y = np.random.randn(8000)

heatmap, xedges, yedges = np.histogram2d(x, y, bins=50)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plt.clf()
plt.imshow(heatmap.T, extent=extent, origin='lower')
plt.title("Heatmap")
plt.show()