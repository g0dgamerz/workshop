class Vechicle:
    category='car' #class attribute

    def __init__(self,color,doors): #initializer
        """ 
        color and doors are inctance attributes
        """
        self.color=color
        self.doors=doors

    def description(self):
        """
        this method returns the description of the object
        """
        return f"This vehicle's color is {self.color} and it has {self.doors} doors."

    def make_it_blue(self):
        """change the color attribute to blue"""
        self.color="blue"

#instantiating an object
rover = Vechicle('red','4')
print(f"Before:{rover.color}")
#this changes the color attribute of object rover
print(rover.description())
rover.make_it_blue()
print(f"After:{rover.color}")
#output will be
#before:red
#This vehicle's color is red and it has 4 doors.
#after:blue


