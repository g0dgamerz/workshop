class Vehicle:
    def __init__(self,color,doors):
        """
        color and doors are instance attributes
        """
        self.color=color
        self.doors=doors

class Car(Vehicle):
    
    def number_of_doors(self):
        return f"Car has {self.doors} doors"

car1= Car("blue",4)
print(car1.color)
print(car1.doors)
print(car1.number_of_doors())