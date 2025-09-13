class Vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price

    def show(self):
        print("Details",self.name,self.color,self.price)

    def max_speed(self):
        print("vehicle max speed is 150")

    def change_gear(self):
        print("Vehicle change 4 gear")

#inherit fron vehicle class
class Car(Vehicle):
    def max_speed(self):  #override methods
        print("The speed of the car is as below")
        print("Car max speed is 240")

    def change_gear(self):#override  method
        print("The gear box details are shown below")
        print("Car change 7 gear")

#car object

car=Car("Kia","Red",20000000)
car.show()
#call method from car class
car.max_speed()
car.change_gear()

#vehicle object
vehicle=Vehicle("Defender","White",100000000)
vehicle.show()

#calls method from a vehicle class
vehicle.max_speed()
vehicle.change_gear()
print("Vehicle class dict: ",Vehicle.__dict__)
print("\nCar class dict: ",Car.__dict__)

        
