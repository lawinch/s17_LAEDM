"""
Method:         Stacked area chart
Data Variables: 1d array of x axis, 2d array of data
Author:         Boris Pleshakov
"""

def stack_area_chart(x, y):
ax = plt.stackplot(x, y)
return ax