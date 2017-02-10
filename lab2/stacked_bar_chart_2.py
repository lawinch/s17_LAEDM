"""
Method:         Stacked bar chart
Data Variables: 2d array of floats
Author:         Boris Pleshakov
"""

def stacked_bar_chart(data, legend, groups):
   
ind = np.arange(len(groups))
width = 0.35
   
cycol = cycle('bgrcmk')
   
plots = list()
   
prev = None
   
for i in range(0, len(data)):
       ax = plt.bar(ind, data[i], width, bottom=prev, color=next(cycol))
   plots.append(res[0])
   prev = data[i]
  
plt.xticks(ind, groups)
plt.legend(plots, legend)
Return ax