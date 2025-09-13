from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

#Defining circle sub class from shape abstract class
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2

    def perimeter(self):
        return 2*3.14*self.radius

class Rectangle(Shape):
    def __init__(self,l,w,):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w

    def perimeter(self):
        return 2*(self.l+self.w)



circle=Circle(3)
AreaC=circle.area()
print("Area of circle: ",AreaC)
perC=circle.perimeter()
print("Perimeter of circle: ",perC)

rectangle=Rectangle(8,4)
AreaR=rectangle.area()
print("Area of Rectangle: ",AreaR)
perR=rectangle.perimeter()
print("Perimeter of Rectangle: ",perR)




