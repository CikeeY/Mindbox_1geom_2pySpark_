import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def length_to_other_point(self, other_point):
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5

class Circle:
 
    def __init__(self, tp1: tuple = (0., 0.), tp2: tuple = (1., 1.)):
        self.pnt1 = Point(*tp1)
        self.pnt2 = Point(*tp2)
 
    def radius(self):
        return self.pnt1.length_to_other_point(self.pnt2)
 
    def area(self):
        return math.pi * (self.radius() ** 2)

class Triangle:
 
    def __init__(self, tp1: tuple = (0., 0.), tp2: tuple = (1., 1.), tp3: tuple = (2., 2.)):
        self.pnt1 = Point(*tp1)
        self.pnt2 = Point(*tp2)
        self.pnt3 = Point(*tp3)
 
    def side1(self):
        return self.pnt1.length_to_other_point(self.pnt2)
 
    def side2(self):
        return self.pnt2.length_to_other_point(self.pnt3)
    
    def side3(self):
        return self.pnt1.length_to_other_point(self.pnt3)
    
    def perimeter(self):
        return (self.side1() + self.side2() + self.side3()) / 2
 
    def area(self, pr=2):
        return (self.perimeter() * (self.perimeter() - self.side1()) * \
                (self.perimeter() - self.side2()) * (self.perimeter() - self.side3())) ** 0.5
    
    def isRight(self):
        side1, side2, side3 = sorted([self.side1(), self.side2(), self.side3()])
        return side1 > 0 and side1 * side1 + side2 * side2 == side3 * side3