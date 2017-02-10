"""
Method:         Scatter plot
Data Variables: 3 variables: 
1st - x points
2nd - y points
3rd - classes of points in colors
Author:         Fattakhova Yulduz
"""

import matplotlib.pyplot as plt
def plot_scatter(x_,y_,colors,size):
   for i in range(size):
       plt.scatter(x_[i], y_[i], color = colors[i])