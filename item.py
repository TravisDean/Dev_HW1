import math
__author__ = 'Travis Dean'

class Item:
    """Keeps track of the dataset items."""
    def __init__(self, x, y, category):
        self.x = float(x)
        self.y = float(y)
        self.category = category

    def distance(self, other):
        return math.sqrt(math.pow((self.x-other.x),2) + math.pow((self.y - other.y),2))

    # def distance(self, x, y):
    #     return math.sqrt(math.pow((self.x-x),2) + math.pow((self.y - y),2))

    def __str__(self):
        return self.category + " " + str(self.x) + " " + str(self.y)

