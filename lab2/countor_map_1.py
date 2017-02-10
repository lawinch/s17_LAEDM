"""
Method:         Countor map
Data Variables: 3 axes: X, Y, Z
Each is series of numbers
Author:         Dmitry Bystritsky
"""

import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
# difference of Gaussians
Z = 10.0 * (Z2 - Z1)

def countor_map(X, Y, Z):
   plt.figure()
   CS = plt.contour(X, Y, Z)
   plt.clabel(CS, inline=1, fontsize=10)
   plt.title('Countor map diagram')

   plt.show()

   
countor_map(X, Y,Z)