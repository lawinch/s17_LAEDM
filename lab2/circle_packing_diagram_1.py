"""
Method:         Circle packing diagram
Data Variables: Random
Author:         Tukhvatov Rustam
"""

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,14,30,4,50]
r=[1000,800, 600, 400, 200] # in points, not data units
fig, ax = plt.subplots(1,1)
ax.scatter(x, y, s=r)
plt.title("Circle packing diagram")
plt.show()