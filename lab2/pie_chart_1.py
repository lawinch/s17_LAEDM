"""
Method:         Pie chart
Data Variables: quantitative
Author:         Vinokurov Marat
"""

import matplotlib.pyplot as plt


def plot_pie(values, labels, colors):
    plt.pie(values, labels=labels, colors=colors,
            autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()


label_list = ['Qiwi', 'Yandex money', 'PayPal']
value_list = [215, 130, 245]
color_list = ['gold', 'yellowgreen', 'lightcoral']
plot_pie(value_list, label_list, color_list)
