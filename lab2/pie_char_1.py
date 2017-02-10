"""
Method:         Pie char
Data Variables: Quantitative and nominal
Author:         Timur Kasatkin
"""

import matplotlib.pyplot as plt


def pie_chart(values, labels):
    plt.figure(1, figsize=(6, 6))
    return plt.pie(values, labels=labels, autopct='%d')


pie_chart([15, 30, 45, 10], ['Frogs', 'Hogs', 'Dogs', 'Logs']);
