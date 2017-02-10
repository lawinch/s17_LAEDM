"""
Method:         Parallel coordinates
Data Variables: 1d array of x axis, 2d array of data
Author:         Boris Pleshakov
"""


def parallel_coordinates(x, data, style=None):


    fig, axes = plt.subplots(1, len(x) - 1, sharey=False)
cycol = cycle('bgrcmk')

colors = list()
for i in range(0, len(data)):
    colors.append(next(cycol) + '-')

for i in range(0, len(axes)):
    for j in range(0, len(data)):
        axes[i].plot(x, data[j], colors[j])
    axes[i].set_xlim([x[i], x[i + 1]])

for axx, xx in zip(axes, x[:-1]):
    axx.xaxis.set_major_locator(ticker.FixedLocator([xx]))
axes[-1].xaxis.set_major_locator(ticker.FixedLocator([x[-2], x[-1]]))  # the last one

for tick in axes[-1].yaxis.get_major_ticks():
    tick.label2On = True

plt.subplots_adjust(wspace=0)

return plt
