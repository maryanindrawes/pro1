# import math

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = self.radius ** 2 * pi  # math.pi
        return area

    def Cir(self):
        cir = 2 * self.radius * pi  # math.pi
        return cir


c1 = Circle(5)
c2 = Circle(10)
print("The area of C1 = ", c1.area())
print("The area of C2 = ", c2.area())
print("The Cir of C1 = ", c1.Cir())
print("The Cir of C1 = ", c2.Cir())
