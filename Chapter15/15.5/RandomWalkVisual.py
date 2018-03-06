#this is the scatter plot

import matplotlib.pyplot as plt

#file and class that I created
from RandomWalk import RandomWalk

#make a random walk, and plot the points
rw = RandomWalk(50000)
rw.fill_walk()

#set the size of the plotting window
plt.figure(figsize=(10,6))

#get number of points in the walk then use to set the color of each point in the walk
pointNumbers = list(range(rw.numPoints))
plt.scatter(rw.xValues, rw.yValues, c=pointNumbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

#emphasize the first and last points
plt.scatter(0,0, c='green', edgecolors='none', s=100)
plt.scatter(rw.xValues[-1], rw.yValues[-1], c='red', edgecolors='none', s=100)

#remove the axes
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()
