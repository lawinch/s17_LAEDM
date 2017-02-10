"""
Method:         Stacked Area Chart
Data Variables: 3 categories - nominal
Y-axis - quantitative(random)
X- axis - quantitative(random)
Author:         Kenneth Nwafor
"""

import numpy as np
import matplotlib.pyplot as plt


def fnx():
return np.random.randint(5, 50, 10)

y = np.row_stack((fnx(), fnx(), fnx()))
x = np.arange(10)

y1, y2, y3 = fnx(), fnx(), fnx()

fig, ax = plt.subplots()
ax.stackplot(x, y)
plt.show()