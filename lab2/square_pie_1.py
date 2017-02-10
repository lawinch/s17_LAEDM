"""
Method:         Square pie
Data Variables: Classes - set of classes (String)
Values - set of data (integer)
Width - integer
Height - integer
Colormap - http://matplotlib.org/examples/color/colormaps_reference.html 
Author:         Mikhail Tilicheev
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def square_pie(classes, values, width, height, colormap, **kwargs):
    class_portion = [float(v) / sum(values) for v in values]
    total_tiles = width * height
    tiles_per_class = [round(p * total_tiles) for p in class_portion]
    plot_matrix = np.zeros((height, width))
    class_index = 0
    tile_index = 0
    for col in range(width):
        for row in range(height):
            tile_index += 1
            if tile_index > sum(tiles_per_class[0:class_index]):
                class_index += 1
            plot_matrix[row, col] = class_index
    plt.matshow(plot_matrix, cmap=colormap)
    plt.colorbar()
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, (width), 1), minor=True);
    ax.set_yticks(np.arange(-.5, (height), 1), minor=True);
    ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
    legend_handles = []
    for i, c in enumerate(classes):
        lable_str = c + " (" + str(values[i]) + ")"
        color_val = colormap(float(i + 1) / len(classes))
        legend_handles.append(mpatches.Patch(color=color_val, label=lable_str))
    plt.legend(handles=legend_handles, loc=1, ncol=len(classes),
               bbox_to_anchor=(0., -0.1, 0.95, .10))
    plt.xticks([])
    plt.yticks([])
    return plt


plot_width = 20
plot_height = 7
classes = ['cat1', 'cat2', 'cat3', 'cat4', 'cat5']
values = [84911, 14414, 10062, 8565, 16000]

square_pie(classes, values, plot_width, plot_height, plt.cm.coolwarm)

plt.show()
