class Box:
    __num=10
    length=None
    breadth=None

    def set_dimensions(self,l,b):
        print(self) #<__main__.Box object at 0x000001D73DD92660>
        self.length=l
        self.breadth=b

        return f'length-{self.length}\t Breadth-{self.breadth}'

    def calculate_area(self):
        area=self.length*self.breadth
        return "Area-{:.2f}".format(area)

boxObj=Box()
print(boxObj)

x=float(input("Enter length \n"))
y=float(input("Enter breadth \n"))
print(boxObj.set_dimensions(x,y))
print(boxObj.calculate_area())
