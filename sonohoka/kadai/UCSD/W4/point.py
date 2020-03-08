import math
class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


