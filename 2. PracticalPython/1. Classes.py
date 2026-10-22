# A class is a blueprint for creating objects. An object contains data and can perform actions through methods.

# Classes and objects -- Concept: A class is a blueprint for creating objects. An object is an instance of a class.

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def start(self):
        print(f"{self.brand} is starting")

car1 = Car("Toyota", "White")
car2 = Car("Honda", "Black")

print(car1.brand)
print(car2.color)

car1.start()
car2.start()

print("----------")


# Understand these four things:

    # class Car: Defines the blueprint.
    # __init__(): Initializes the object when it is created.
    #  self: Refers to the current object.
    # car1 and car2: Two separate objects created from the same class.
# ----------------------------------


