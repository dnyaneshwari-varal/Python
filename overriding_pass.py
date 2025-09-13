'''
if you dont want to print in function inside of empty function we write pass keyword

#code1
class Vehicle:
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")

class Car(Vehicle):
    # Overriding 'stop' but not adding functionality yet
    def stop(self):
        pass 
# Usage
c = Car()
c.start()   
c.stop()   
'''
#code2
class Vehicle:
    def horn(self):
        print("Beep! Beep!")

class ElectricCar(Vehicle):
    # Electric car is silent, so disable horn
    def horn(self):
        pass

# Usage
ec = ElectricCar()
ec.horn()  

