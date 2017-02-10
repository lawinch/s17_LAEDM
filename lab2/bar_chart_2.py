"""
Method:         Bar chart
Data Variables: List of names/objects and corresponding values
Author:         Anastasiia Krasnoshchekova
"""

import matplotlib.pyplot as plt

plt.rcdefaults()
import numpy as np


def bar_chart(objects, performance, xlabel='', ylabel='', title='', **kwargs):
    y_pos = np.arange(len(objects))
    objects_performance = zip(objects, performance)
    objects_performance = sorted(objects_performance, key=lambda t: t[1])
    objects1, performance1 = zip(*objects_performance)

    plt.barh(y_pos, performance1, align='center', alpha=0.5)
    plt.yticks(y_pos, objects1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    return plt


# example
bar_chart(['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp'], [6, 8, 10, 4, 2, 1], 'Usage', '',
          'Programming language usage')
plt.show()
