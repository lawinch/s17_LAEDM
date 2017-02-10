"""
Method:         Pie chart
Data Variables: 2 variables: labels and quantitative number for each label
Author:         Fattakhova Yulduz
"""

Import
matplotlib.pyplot.pie


def plot_pie_chart(labels, fracs):
    figure(1, figsize=(6, 6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    explode = (0, 0.05, 0, 0)

    pie(fracs, explode=explode, labels=labels,
        autopct='%1.1f%%', shadow=True, startangle=90)
    show()
