#operator overloading

class Book:
    def __init__(self,pages):
        self.pages=pages

    #operator overloading with magic method
    def __add__(self,other):
        return self.pages + other.pages
b1=Book(400)
b2=Book(300)

print("Total number of pages: ",b1+b2)



#example2
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #overload operator with magic method
    def __lt__(self,other):
        return self.age < other.age

p1=Person("Sham",21)
p2=Person("Prem",23)
print(p1 < p2)
print(p2 < p1)


