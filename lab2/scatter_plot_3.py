"""
Method:         Scatter Plot
Data Variables: numbers
Author:         Adayev Marat
"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as pl

def get_data():
   data = pd.read_csv('user_bq_data.csv')
   data = data[(pd.notnull(data['user_id'])) & (pd.notnull(data['age']))]
   return [list(map(int, data.user_id.values.tolist())),list(map(int, data.age.values.tolist()))];

def scatter_plot(values):
   fig, ax = pl.subplots()
   x = values[0]
   y = values[1]
   ax.scatter(x, y)
   
scatter_plot(get_data())
pl.show()