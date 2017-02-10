"""
Method:         Histogram
Data Variables: quantitative
Author:         Vinokurov Marat
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_hist(values, title=None, xlabel=None, ylabel=None):
  plt.hist(values)
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.show()

plot_hist(np.random.randn(1000), "Gaussian Histogram", "Value", "Frequency")