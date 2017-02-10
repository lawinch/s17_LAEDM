"""
Method:         Contour map
Data Variables: projection, resolution - string

others - quantitative 
Author:         Vladimir Shevchenko
"""

#conda install -c anaconda basemap
import mpl_toolkits.basemap as bm
import matplotlib.pyplot as plt
import numpy as np

def contour_map(projection, lat_0, lon_0, resolution, lats, lons, wave, mean):

    map = bm.Basemap(projection = projection, lat_0 = lat_0, lon_0 = lon_0, resolution = resolution)
    #coastlines and countries
    map.drawcoastlines(linewidth = 0.25)
    map.drawcountries(linewidth = 0.25)
    map.fillcontinents(color='coral',lake_color='aqua')
    #edges of map projections
    map.drawmapboundary(fill_color='aqua')
    #lines
    map.drawmeridians(np.arange(0, 360, 30))
    map.drawparallels(np.arange(-90, 90, 30))

    x, y = map(lons *180./np.pi, lats*180./np.pi)
    #contours
    map.contour(x, y, wave + mean, 15 ,linewidths=1.5)

    return plt

#data
nlats = 73; nlons = 145; delta = 2.*np.pi/(nlons-1)
lats = (0.5*np.pi-delta*np.indices((nlats,nlons))[0,:,:])
lons = (delta*np.indices((nlats,nlons))[1,:,:])
wave = 0.75*(np.sin(2.*lats)**8*np.cos(4.*lons))
mean = 0.5*np.cos(2.*lats)*((np.sin(2.*lats))**2 + 2.)

plot = contour_map('ortho', 45, -100, 'l', lats, lons, wave, mean)
plot.show()