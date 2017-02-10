"""
Method:         Stacked area chart
Data Variables: 2 variables:
1st - x points 
2nd - arrays of y points for every line
Author:         Fattakhova Yulduz
"""

import matplotlib.pyplot as plt

def fnx():
   return np.random.randint(5, 50, 10)

y_ = np.row_stack((fnx(), fnx(), fnx()))
x_ =  np.arange(10)


def plot_stacked_area_chart(x_,y_):
   fig, ax = plt.subplots()
   ax.stackplot(x_, y_)
   plt.show()