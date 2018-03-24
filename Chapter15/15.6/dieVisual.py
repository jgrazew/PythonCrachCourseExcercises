import pygal
from die import Die

#create 2 D6 die
die1 = Die()
die2 = Die()

results = [(die1.roll() + die2.roll()) for rollNum in range(10000)]

frequencies = [results.count(value) for value in range(2, maxResult+1)]

hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = [xlabel for xlabel in range(2,maxResult+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)

hist.render_to_file('C:\\Users\\Joe\\Documents\\die_visual.svg')
