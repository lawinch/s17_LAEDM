"""
Method:         Stacked bar chart
Data Variables: There are several variables: 1 variable is quantitative and other 3 are nominal (or they can be ordinal)
Author:         Vladislav Lipatov
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def stacked_bar_chart(data=None):
    if data is None:
        data = pd.DataFrame(np.random.rand(10, 3), columns=['answer1', 'answer2', 'answer3'])
    data.plot(kind='bar', stacked=True)
    plt.show()


stacked_bar_chart()
