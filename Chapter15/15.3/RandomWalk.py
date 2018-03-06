from random import choice 

class RandomWalk():
    """A class that generates random walks"""

    def __init__(self, numPoints=5000):
        """initializes attributes of a walk"""
        self.numPoints = numPoints

        #All walks start at (0,0)
        self.xValues = [0]
        self.yValues = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""

        #keep taking steps until the walk reaches the desired length
        #random.choice will slect a number randomly from our list
        while len(self.xValues) < self.numPoints:
            #Decide which direction to go and how far to goin that direction
            xDirection = choice([1,-1])
            xDistance  = choice([0,1,2,3,4])
            xStep = xDirection*xDistance

            yDirection = choice([1,-1])
            yDistance = choice([0,1,2,3,4])
            yStep = yDirection * yDistance

            #reject moves that go nowhere
            if xStep == 0 and yStep == 0:
                continue

            #calculate the next x and y values
            #index -1 list returns the last value
            nextX = self.xValues[-1] + xStep
            nextY = self.yValues[-1] + yStep

            self.xValues.append(nextX)
            self.yValues.append(nextY)

