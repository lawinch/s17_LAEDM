"""
Method:         Ring chart
Data Variables: Texts, numbers
Author:         Dmitry Mordovtsev
"""

import matplotlib.pyplot as plt

def ring_chart(sizes, text, colors, labels):
   col = colors
   fig, ax = plt.subplots()
   ax.axis('equal')
   width = 0.35
   kwargs = dict(colors=col, startangle=180)
   outside, _ = ax.pie(sizes, radius=1, pctdistance=1-width/2,labels=sizes,**kwargs)
   plt.setp(outside, width=width, edgecolor='white')

   kwargs = dict(size=20, fontweight='bold', va='center')
   ax.text(0, 0, text, ha='center', **kwargs)
   patches, texts = plt.pie(sizes, colors=colors, startangle=90)
   centre_circle = plt.Circle((0, 0), 0.75, color='black', fc='white', linewidth=1.25)
   fig = plt.gcf()
   fig.gca().add_artist(centre_circle)
   legends = map((lambda x, y: x + ' ' + str(y) + ' %'), labels, sizes)
   plt.legend(patches, legends, loc="best")
   # Set aspect ratio to be equal so that pie is drawn as a circle.
   plt.axis('equal')
   plt.tight_layout()
   plt.show()

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
countries = ['Russia', 'Switzerland', 'Canada', 'France']

ring_chart([20, 30, 35, 15], "Unemployment rate", colors, countries)