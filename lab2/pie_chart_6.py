"""
Method:         Pie chart
Data Variables: List of names (string) and list of values (int/float) 
Author:         Anastasiia Krasnoshchekova
"""

import matplotlib.pyplot as plt
import numpy as np

def pie_chart(labels, sizes, title = '', **kwargs):
  cmap = plt.get_cmap('gnuplot')
  colors = [cmap(i) for i in np.linspace(0.1, 1, len(labels))]
  patches, texts = plt.pie(sizes, colors=colors)
  plt.legend(patches, labels, loc="best")
  plt.axis('equal')
  plt.title(title)
  plt.tight_layout()
  return plt

# example
labels = ['Cookies', 'Jellybean', 'Milkshake', 'Cheesecake']
sizes = [38.4, 40.6, 20.7, 10.3]
pie_chart(labels, sizes, 'Pie chart')
plt.show()