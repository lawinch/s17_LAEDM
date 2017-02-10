"""
Method:         Scatter chart
Data Variables: There are 4 quantitative variables (that actually are represented in 2-dimension space) and 2 nominal variables that represent groups
Author:         Vladislav Lipatov
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def scatter_chart(data=None):
  if data is None:
      data = pd.DataFrame(np.random.rand(20, 4), columns=['feature1', 'feature2', 'feature3', 'feature4'])
  ax = data.plot.scatter(x='feature1', y='feature2', color='red', label='Group1')
  data.plot.scatter(x='feature3', y='feature4', color='green', label='Group2', ax=ax)
  plt.show()

scatter_chart()