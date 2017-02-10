"""
Method:         Tornado diagram
Data Variables: 3 main variables:
x_left - quantitative (data for left side)
x_right - quantitative (data for right side)
y - set of labels
Author:         Mikhail Tilicheev
"""

import matplotlib.pyplot as plt
import numpy as np


def tornado_diagram(x_left, x_right, y, x_left_label=None, x_right_label=None, title=None, **kwargs):
    num_y = len(y)
    max_size = len(max(y))
    x_sp = -0.2
    w_sp = 0.5
    if max_size > 10:
        n = int(max_size / 10)
        for i in range(n):
            x_sp = (x_sp * 2 - 0.05);
            w_sp *= 2

    pos = np.arange(num_y) + .5  # bars centered on the y axis
    fig, (ax_left, ax_right) = plt.subplots(ncols=2, **kwargs)

    ax_left.barh(pos, x_left, align='center', facecolor='cornflowerblue')
    ax_left.set_yticks([])
    ax_left.set_xlabel(x_left_label)
    ax_left.invert_xaxis()

    ax_right.barh(pos, x_right, align='center', facecolor='lemonchiffon')
    ax_right.set_yticks(pos)
    ax_right.set_yticklabels(y, ha='center', x=x_sp)
    ax_right.set_xlabel(x_right_label)
    fig.suptitle(title)
    fig.subplots_adjust(wspace=w_sp)
    return fig


tornado_diagram((15, 20, 10), (146, 67, 210), ('First', 'Second', 'Third'), 'Left Label Text by X',
                'Right Label Text by X', 'Text title')
plt.show()
