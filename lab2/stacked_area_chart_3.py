"""
Method:         Stacked Area Chart
Data Variables: quantitative 
Author:         Adayev Marat
"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as pl

def get_data():
   data = pd.read_csv('user_bq_data.csv')
   data = data[(pd.notnull(data['LS_1'])) & (pd.notnull(data['LS_2'])) & (pd.notnull(data['LS_3'])) & (data['LS_1'] <= '9') & (data['LS_2'] <= '9') & (data['LS_3'] <= '9')]
   return [list(map(int, data.LS_1.values.tolist())),list(map(int, data.LS_2.values.tolist())),list(map(int, data.LS_3.values.tolist()))];

def stacked_area_chart(values):
   y = np.row_stack((values[0][:10], values[1][:10], values[2][:10]))
   x = np.arange(10)
   fig, ax = pl.subplots()
   ax.stackplot(x, y)
   
stacked_area_chart(get_data())
pl.show()