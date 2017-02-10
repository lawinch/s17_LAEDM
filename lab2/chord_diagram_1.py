"""
Method:         Chord diagram
Data Variables: List of string
List of number (like example data)
One more example data:
[[0, 0, 32, 17, 23],
[0, 0, 19, 5, 14],
[32, 19, 0, 0, 0],
[17, 5, 0, 0, 0],
[23, 14, 0, 0, 0]]
Author:         Mikhail Tilicheev
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import math


def chord_chart(values, labels, **args):
    x = len(values[0])
    getval = [sum(i) for i in values]
    fig, ax = plt.subplots()
    ax.axis('equal')
    chart, _ = ax.pie(getval, radius=1)
    plt.setp(chart, width=0.05, edgecolor='white', **args)
    ax.legend(chart, labels, frameon=False, bbox_to_anchor=(1, 1),
              bbox_transform=plt.gcf().transFigure)
    sumval = sum(getval)
    newalpha = 0
    rad = 2 * math.pi / sumval
    patches = []
    for i in range(x // 2):
        for j in range(x // 2, x):
            if (values[i][j] != 0):
                alpha = newalpha + values[i][j]
                newbetha = sum([sum(values[k]) for k in range(j)])
                if (i > 0):
                    for k1 in range(i):
                        newbetha += values[j][k1]
                betha = newbetha + values[j][i]
                Path = mpath.Path
                partA6 = (alpha - newalpha) / 6
                partB6 = (betha - newbetha) / 6
                path_data = [
                    (Path.MOVETO, [math.cos(rad * newalpha), math.sin(rad * newalpha)]),
                    (Path.CURVE4, [math.cos(rad * (newalpha + partA6)), math.sin(rad * (newalpha + partA6))]),
                    (Path.CURVE4, [math.cos(rad * (newalpha + 2 * partA6)), math.sin(rad * (newalpha + 2 * partA6))]),
                    (Path.CURVE4, [math.cos(rad * (newalpha + 3 * partA6)), math.sin(rad * (newalpha + 3 * partA6))]),
                    (Path.CURVE4, [math.cos(rad * (newalpha + 4 * partA6)), math.sin(rad * (newalpha + 4 * partA6))]),
                    (Path.CURVE4, [math.cos(rad * (newalpha + 5 * partA6)), math.sin(rad * (newalpha + 5 * partA6))]),
                    (Path.CURVE4, [math.cos(rad * alpha), math.sin(rad * alpha)]),
                    (Path.CURVE3, [0, 0]),
                    (Path.CURVE3, [math.cos(rad * newbetha), math.sin(rad * newbetha)]),
                    (Path.CURVE4, [math.cos(rad * (newbetha + partB6)), math.sin(rad * (newbetha + partA6))]),
                    (Path.CURVE4, [math.cos(rad * (newbetha + 2 * partB6)), math.sin(rad * (newbetha + 2 * partB6))]),
                    (Path.CURVE4, [math.cos(rad * (newbetha + 3 * partB6)), math.sin(rad * (newbetha + 3 * partB6))]),
                    (Path.CURVE4, [math.cos(rad * (newbetha + 4 * partB6)), math.sin(rad * (newbetha + 4 * partB6))]),
                    (Path.CURVE4, [math.cos(rad * (newbetha + 5 * partB6)), math.sin(rad * (newbetha + 5 * partB6))]),
                    (Path.CURVE4, [math.cos(rad * betha), math.sin(rad * betha)]),
                    (Path.CURVE3, [0, 0]),
                    (Path.CURVE3, [math.cos(rad * newalpha), math.sin(rad * newalpha)]),
                    (Path.CLOSEPOLY, [math.cos(rad * newalpha), math.sin(rad * newalpha)])
                ]
                codes, verts = zip(*path_data)
                path = mpath.Path(verts, codes)
                patch = mpatches.PathPatch(path)
                patches.append(patch)
                newalpha = alpha

    colors = np.linspace(0, 1, len(patches))
    collection = PatchCollection(patches, cmap=plt.cm.Accent, alpha=0.7)
    collection.set_array(np.array(colors))
    ax.add_collection(collection)

    plt.axis('equal')
    plt.axis('off')
    # full screen mode
    # mng = plt.get_current_fig_manager()
    # mng.full_screen_toggle()
    return ax


# Example data
labels = ['Hardware', 'Software', 'Services', 'new']
values = [[0, 0, 32, 17],
          [0, 0, 19, 5],
          [32, 19, 0, 0],
          [17, 5, 0, 0]]

chord_chart(values, labels)

plt.show()
