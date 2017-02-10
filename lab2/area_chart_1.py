"""
Method:         Area chart
Data Variables: There are 1 quantitative variable and 1 nominal variable (we can transform this chart into stacked area chart by adding more nominal variables)
Author:         Vladislav Lipatov
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def area_chart(data=None):
  if data is None:
      data = pd.DataFrame(np.random.rand(10, 1), columns=['item1'])
  data.plot.area()
  plt.show()

area_chart()