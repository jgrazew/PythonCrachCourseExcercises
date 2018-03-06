from random import choice 

class RandomWalk():
    """A class that generates random walks"""

    def __init__(self, numPoints=5000):
        """initializes attributes of a walk"""
        self.numPoints = numPoints

        #All walks start at (0,0)
        self.xValues = [0]
        self.yValues = [0]

    def getStep(self):
        """get direction and step size for the walk"""
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4])
        step = direction * distance
        return step

    def fill_walk(self):
        """Calculate all the points in the walk"""

        #keep taking steps until the walk reaches the desired length
        #random.choice will slect a number randomly from our list
        while len(self.xValues) < self.numPoints:
            #Decide which direction to go and how far to goin that direction; if you get rid of the negative one then it will only be able to go one direction and will look like a line graph
            xStep = self.getStep()

            yStep = self.getStep()

            #reject moves that go nowhere
            if xStep == 0 and yStep == 0:
                continue

            #calculate the next x and y values
            #index -1 list returns the last value
            nextX = self.xValues[-1] + xStep
            nextY = self.yValues[-1] + yStep

            self.xValues.append(nextX)
            self.yValues.append(nextY)

