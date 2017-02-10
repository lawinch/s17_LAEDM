"""
Method:         Stacked bar
Data Variables: 2 type variables:
Columns - type list
Labels - type list(legend of chart)
Author:         Rodionova Anastasia
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_stacked_bar(labels, *y):
   if len(y) == size(labels):
       df = pd.DataFrame(np.transpose(np.array(y)), columns=labels)
       df.plot.barh(stacked=True)

y1 = [7,8,6,11,7]
y2 =   [2,3,4,3,2]
y3 =  [7,8,7,2,2]
labels=['1','2','3']

plot_stacked_bar(labels, y1, y2, y3)