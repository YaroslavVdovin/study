from math import sqrt
class Point:
    def __init__(self, x=0, y=0,):
        self.x = x
        self.y = y

    def set_y_axis(self, y):
        self.y = y

    def set_x_axis(self, x):
        self.x = x

    def distance(self, point):
        return sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
    def __repr__(self):
        return "Ваша точка: %s, %s" % (self.x, self.y)


firstloc = Point(1, 2)
secloc = Point(5, 6)

print(secloc.distance(firstloc))