"""
Method:         Bubble Plot map
Data Variables: lat - set of latitude
lon - set of longitude
area - set of data
colors - set of colors
title - set of titles
Author:         Mikhail Tilicheev
"""

import matplotlib.pyplot as plt

def area_to_per(area, m):
  per100 = max(area)
  for i in range(len(area)):
      area[i] = area[i]*m/per100;
  return area

def bubble_plot(x, y, area, colors, title, m=100, **kwargs):
  areas = area_to_per(area, m)
  plt.scatter(x, y, s=areas, c=colors, alpha=0.5, **kwargs)
  for i in range (len(x)):
      plt.text(x[i], y[i], title[i], fontsize=10, ha='center')
  plt.grid()
  return plt

#Example data
title=['Russia', 'USA', 'Canada', 'China', 'Brazil']
lat = [55.45, 38.53, 45.24, 39.55, -15.46] #Latitude
lon = [37.36, -77.02, -75.41, 116.24, -47.55] #Longitude
colors = ['r', 'b', 'g', 'y', 'c']
area = [17100000, 9834000, 9985000, 9597000, 8516000]

bubble_plot(lon, lat, area, colors, title, 15000)
plt.show()