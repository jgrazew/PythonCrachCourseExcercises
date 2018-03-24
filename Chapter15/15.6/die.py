from random import randint 

class Die():
    """A class representing a single die"""

    def __init__(self, numSides=6):
        """Assume a six sided die if nothing is passed in"""
        self.numSides = numSides

    def roll(self):
        """return a random value between 1 and the number of sides"""
        return randint(1, self.numSides)
