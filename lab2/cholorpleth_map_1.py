"""
Method:         Cholorpleth map
Data Variables: There are quantitative data (gdp data for countries, population data for countries) and nominal data (names of the countries)
Author:         Vladislav Lipatov
"""

import matplotlib.pyplot as plt
import geopandas as geo


def choropleth_map():
    world = geo.read_file(geo.datasets.get_path('naturalearth_lowres'))
    world = world[(world.pop_est > 0) & (world.name != "Antarctica")]
    world['gdp_per_cap'] = world.gdp_md_est / world.pop_est
    world.plot(column='gdp_per_cap')
    plt.show()


choropleth_map()
