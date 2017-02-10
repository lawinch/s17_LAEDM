"""
Method:         Stacked area chart
Data Variables: x - nominal (e.g. years),
ys - list of ratio variables
labels - names of ratio variables
Author:         Timur Kasatkin
"""

# https://plot.ly/python/
# pip install plotly
# register and write login and api key into folder ".plotly/.credentials" which inside os user's home folder

import plotly.plotly as py
import plotly.graph_objs as go

def stacked_area_chart(x, ys, labels):
  data = list(map(lambda t:
                  go.Scatter(x=x,
                             y=t[0],
                             text=list(map(lambda y: '%d%%' % y, t[0])),
                             hoverinfo='x+text',
                             mode='lines',
                             line=dict(width=0.5),
                             fill='tonexty',
                             name=t[1]),
                  zip(ys, labels)))
  return go.Figure(data=data)

fig = stacked_area_chart(x=['Winter', 'Spring', 'Summer', 'Fall'],
                       ys=[[40, 20, 30, 40],
                           [50, 70, 40, 60],
                           [70, 80, 60, 70],
                           [100, 100, 100, 100]],
                       labels=['Television', 'Newspaper', 'Radio', 'Internet'])
py.iplot(fig)