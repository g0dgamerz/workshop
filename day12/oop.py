class Vechcle:
    category='car' #class attribute

    def __init__(self,color,doors): #initializer
        """
        color and doors are instance attributes
        """
        self.color=color
        self.doors=doors

#instantiating an object
rover = Vechcle('red','4')
#printing instance attribute
print(f'Vehicle color: {rover.color}')
#printing class attribute
print(f'Vehicle category:{rover.category}')
print(f'Number of doors: {rover.doors}')

#we can access the class attributes this way too
print(f'category:{rover.__class__.category}')