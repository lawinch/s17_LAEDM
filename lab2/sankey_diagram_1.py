"""
Method:         Sankey diagram
Data Variables: quantitative and nominal
Author:         Adayev Marat
"""

import matplotlib.pyplot as pl
from matplotlib.sankey import Sankey


def sankey_diagram():
    sankey = Sankey()
    sankey.add(flows=[2, -4.5, 0.5, 1, 1],
               orientations=[0, 0, 1, -1, 1],
               labels=['input1', 'output', 'input2', 'input3', 'input4'],
               rotation=0)
    sankey.finish()


sankey_diagram()
pl.show()
