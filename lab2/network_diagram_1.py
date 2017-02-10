"""
Method:         Network diagram
Data Variables: nodes - nominal

edges - connections between nodes
Author:         Vladimir Shevchenko
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import random as rnd

def plot_network_diagram(nodes, edges):
   radius = 20
   size = 1000
   colors = ['red', 'green', 'blue', 'yellow']
   #size of area
   axis = plt.gca()
   axis.set_xlim((0, size + radius))
   axis.set_ylim((0, size + radius))
   #positions of nodes
   node_pos = {}
   #draw nodes
   for node in nodes:
       #get random coordinate
       x = rnd.randint(radius, size)
       y = rnd.randint(radius, size)
       circle = plt.Circle((x, y), radius, 
           color = rnd.choice(colors))
       axis.add_artist(circle)
       plt.text(x, y, node, 
           verticalalignment = 'center',
           horizontalalignment = 'center')
       node_pos[node] = (x, y)
   #draw edges    
   axis.grid(zorder = 0)
   for node1 in edges:
       for node2 in edges[node1]:
           xs = (node_pos[node1][0], node_pos[node2][0])
           ys = (node_pos[node1][1], node_pos[node2][1])
           #draw line
           line = lines.Line2D(xs, ys, linewidth=1, color='black', zorder = 1)
           axis.add_line(line)     

   plt.axis('off')
   return plt

#data
node_count = 50
edge_count = 40

nodes = np.arange(node_count)
#generate edges
edges = {}
for i in range(edge_count):
   node1 = rnd.choice(nodes)
   node2 = rnd.choice(nodes)
   if node1 not in edges:
       edges[node1] = []
       edges[node1].append(node2)  

plot = plot_network_diagram(nodes, edges)
plot.show()