"""
Method:         Area chart
Data Variables: 2 variables:
X - axes
Y - stack of 3 lines of data (y1,y2,y3)ß
Author:         Dmitry Bystritsky
"""

import numpy as np
import matplotlib.pyplot as plt


def fnx():
    return np.random.randint(5, 50, 10)


y = np.row_stack((fnx(), fnx(), fnx()))
x = np.arange(10)


def two_area_charts(x, y):
    fig, ax = plt.subplots()
    ax.stackplot(x, y)
    plt.show()


two_area_charts(x, y)
