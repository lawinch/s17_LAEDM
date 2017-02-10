"""
Method:         Histogram
Data Variables: 1 variable is quantitative and another is nominal
Author:         Vladislav Lipatov
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def histogram_chart(data=None):
  if data is None:
      data = pd.DataFrame({'feature1': np.random.randn(100)}, columns=['feature1'])
  data.plot(kind='hist')
  plt.show()

histogram_chart()