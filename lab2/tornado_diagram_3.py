"""
Method:         Tornado diagram
Data Variables: categories - names of categories, strings

left_values and right_values - quantitative
Author:         Vladimir Shevchenko
"""

import random as rnd
import numpy as np
import matplotlib.pyplot as plt

#values should be positive!
def plot_tornado(categories, left_values, right_values):
   height = 1
   char_size = 50
   max_text_size = 500
   max_width = max(max(left_values), max(right_values)) + max_text_size
   #ys from top to bottom
   ys = range(len(left_values))[::-1]  
   for y, left_width, right_width in zip(ys, left_values, right_values):
       #draw left bar and text
       text = '%1.1f' % left_width
       text_size = len(text) * char_size
       plt.bar(-left_width, height, left_width, y, color = 'blue')
       plt.text(-left_width - text_size, y, text)
       #draw right bar and text
       text = '%1.1f' % right_width
       plt.bar(0, height, right_width, y, color = 'green')
       plt.text(right_width, y, text)
   #middle line
   plt.axvline(0, color='black')
   #axes 
   axes = plt.gca() 
   axes.xaxis.set_ticks_position('top')
   #display categories on y axis
   plt.ylim(-1, len(categories))
   plt.yticks(ys, categories)
   #setup x axis
   plt.xlim(-max_width, max_width)
   #make absolute values for x axis
   abs_ticks = [abs(tick) for tick in axes.get_xticks()]
   plt.xticks(axes.get_xticks()[1:-1], abs_ticks[1:-1])
   return plt

#data 
n =  10
max_value = 1000
categories = ['Category ' + str(i) for i in range(n)]
left_values = np.random.randint(0, max_value, n)
right_values = np.random.randint(0, max_value, n)

plot = plot_tornado(categories, left_values, right_values)
plot.show()