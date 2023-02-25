import math

from inheretance.Circle import Circle


class Ball(Circle):
    # def __init__(self, radius):
    #     self.radius = radius

    def volume(self):
        v = (4 / 3) * math.pi * self.radius ** 3
        return v

    def area(self):
        return 4 * math.pi * self.radius ** 2
    def print_area(self):
        print("The area is : ", super().area())
