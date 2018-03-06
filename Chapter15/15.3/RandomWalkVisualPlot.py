#question 15-3 replacing plt.scatter() with plt.plot()

import matplotlib.pyplot as plt

#file and class that I created
from RandomWalk import RandomWalk

#make a random walk, and plot the points
rw = RandomWalk()
rw.fill_walk()

#set the size of the plotting window
plt.figure(figsize=(10,6))

#get number of points in the walk then use to set the color of each point in the walk
pointNumbers = list(range(rw.numPoints))
plt.plot(rw.xValues, rw.yValues, linewidth=1, zorder=1)

#emphasize the first and last points; still use scatter for these points; set zorder higher then the plot so that it appears above
plt.scatter(0,0, c='green', edgecolors='none', s=100, zorder=2)
plt.scatter(rw.xValues[-1], rw.yValues[-1], c='red', edgecolors='none', s=100, zorder=2)

#remove the axes
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()

