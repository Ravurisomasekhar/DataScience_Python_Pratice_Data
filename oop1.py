#  Module: Inheritance Assignments
# ## Lesson: Single and Multiple Inheritance
# ### Assignment 1: Single Inheritance Basic
# Create a base class named `Animal` with attributes `name` and `species`. Create a derived class named `Dog` that inherits
#  from `Animal` and adds an attribute `breed`. Create an object of the `Dog` class and print its attributes.

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
# class Dog(Animal):
#     def __init__(self, name, species, breed):
#         super().__init__(name, species)
#         self.breed = breed

# dog = Dog("Buddy", "Canine", "Golden Retriever")
# print(f"Name: {dog.name}, Species: {dog.species}, Breed: {dog.breed}")



# ### Assignment 2: Method Overriding in Single Inheritance
# In the `Dog` class, override the `__str__` method to return a string representation of the object. Create an object of the 
# class and print it.

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

# class Dog(Animal):
#     def __init__(self, name, species, breed):
#         super().__init__(name, species)
#         self.breed = breed

#     def __str__(self):
#         return f"Dog(Name: {self.name}, Species: {self.species}, Breed: {self.breed})"

# dog = Dog("Buddy", "Canine", "Golden Retriever")
# print(dog)


# ### Assignment 3: Single Inheritance with Additional Methods
# In the `Dog` class, add a method named `bark` that prints a barking sound. Create an object of the class and call the method.


# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

# class Dog(Animal):
#     def __init__(self, name, species, breed):
#         super().__init__(name, species)
#         self.breed = breed

#     def bark(self):
#         print(f"{self.name} says Woof!")

# dog = Dog("Buddy", "Canine", "Golden Retriever")
# dog.bark()

# ### Assignment 4: Multiple Inheritance Basic
# Create a base class named `Walker` with a method `walk` that prints a walking message.
#  Create another base class named `Runner` with a method `run` that prints a running message.
#  Create a derived class named `Athlete` that inherits from both `Walker` and `Runner`. Create an object of 
# the `Athlete` class and call both methods.

# class Walker:
#     def walk(self):
#         print("Athlete is walking")
# class Runner:
#     def run(self):
#         print("Athlete is running")
# class Athlete(Walker, Runner):
#     pass

# athlete = Athlete()
# athlete.walk()
# athlete.run()

# ### Assignment 5: Method Resolution Order (MRO) in Multiple Inheritance
# In the `Athlete` class, override the `walk` method to print a different message. Create an object of the class and call the 
# `walk` method. Use the `super()` function to call the `walk` method of the `Walker` class.

# class Walker:
#     def walk(self):
#         print("Athlete is walking")
# class Runner:
#     def run(self):
#         print("Athlete is running")
# class Athlete(Walker, Runner):
#     def walk(self):
#         print("Athlete starts walking.")
#         super().walk()   
# # Create an object
# athlete = Athlete()
# # Call the methods
# athlete.walk()
# athlete.run()
# print("\nMethod Resolution Order (MRO):")
# print(Athlete.mro())

# ### Assignment 6: Multiple Inheritance with Additional Attributes
# In the `Athlete` class, add an attribute `training_hours` and a method `train` that prints the training hours. 
# Create an object of the class and call the method.

# class Walker:
#     def walk(self):
#         print("Athlete is walking")


# class Runner:
#     def run(self):
#         print("Athlete is running")


# class Athlete(Walker, Runner):
#     def __init__(self, training_hours):
#         self.training_hours = training_hours

#     def train(self):
#         print(f"Training Hours: {self.training_hours} hours")
# athlete = Athlete(90)

# athlete.walk()
# athlete.run()
# athlete.train()

# ### Assignment 7: Diamond Problem in Multiple Inheritance
# Create a class named `A` with a method `show` that prints a message. Create two derived classes `B` and `C` that 
# inherit from `A` and override the `show` method. Create a class `D` that inherits from both `B` and `C`. 
# Create an object of the `D` class and call the `show` method. Observe the method resolution order.

# class A:
#     def show(self):
#         print("This is show() method from class A")
# class B(A):
#     def show(self):
#         print("This is show() method from class B")
# class C(A):
#     def show(self):
#         print("This is show() method from class C")
# class D(B, C):
#     pass
# obj = D()
# obj.show()
# print(D.__mro__

# ### Assignment 8: Using `super()` in Single Inheritance
# Create a base class named `Shape` with an attribute `color`. Create a derived class named `Circle` that inherits from `Shape` 
# and adds an attribute `radius`. Use the `super()` function to initialize the attributes. Create an object of the `Circle` class 
# and print its attributes.

# class Shape:
#     def __init__(self, color):
#         self.color = color
# class Circle(Shape):
#     def __init__(self, color, radius):
#         super().__init__(color)
#         self.radius = radius
# circle = Circle("Red", 8)
# print("Color :", circle.color)
# print("Radius:", circle.radius)

# ### Assignment 9: Using `super()` in Multiple Inheritance
# Create a class named `Person` with an attribute `name`. Create a class named `Employee` with an attribute `employee_id`. 
# Create a derived class `Manager` that inherits from both `Person` and `Employee`. Use the `super()` function to initialize the 
# attributes. Create an object of the `Manager` class and print its attributes.

# class Person:
#     def __init__(self, name, **kwargs):
#         super().__init__(**kwargs)
#         self.name = name
# class Employee:
#     def __init__(self, employee_id, **kwargs):
#         super().__init__(**kwargs)
#         self.employee_id = employee_id
# class Manager(Person, Employee):
#     def __init__(self, name, employee_id):
#         super().__init__(name=name, employee_id=employee_id)
# manager = Manager("Somu", 143)
# print("Name:", manager.name)
# print("Employee ID:", manager.employee_id)

# ### Assignment 10: Method Overriding and `super()`
# Create a class named `Vehicle` with a method `start` that prints a starting message. Create a derived class `Car` that overrides
#  the `start` method to print a different message. Use the `super()` function to call the `start` method of the `Vehicle` class. 
# Create an object of the `Car` class and call the `start` method.

# # Parent class
# class Vehicle:
#     def start(self):
#         print("Vehicle has been started.")


# # Child class
# class Car(Vehicle):
#     def start(self):
#         super().start()
#         print("Car has been started and is ready to drive.")
# car = Car()
# car.start()

# ### Assignment 11: Multiple Inheritance with Different Methods
# Create a class named `Flyer` with a method `fly` that prints a flying message.
#  Create a class named `Swimmer` with a method `swim` that prints a swimming message. 
# Create a derived class `Superhero` that inherits from both `Flyer` and `Swimmer`.
#  Create an object of the `Superhero` class and call both methods.

# Assignment 11: Multiple Inheritance with Different Methods

# class Flyer:
#     def fly(self):
#         print("The superhero is flying in the sky!")

# class Swimmer:
#     def swim(self):
#         print("The superhero is swimming in the water!")

# class Superhero(Flyer, Swimmer):
#     pass
# hero = Superhero()
# hero.fly()
# hero.swim()

# ### Assignment 12: Complex Multiple Inheritance
# Create a class named `Base1` with an attribute `a`. Create a class named `Base2` with an attribute `b`. 
# Create a class named `Derived` that inherits from both `Base1` and `Base2` and adds an attribute `c`. 
# Initialize all attributes using the `super()` function. Create an object of the `Derived` class and print its attributes.

# class Base1:
#     def __init__(self, a):
#         self.a = a

# class Base2:
#     def __init__(self, b):
#         self.b = b

# class Derived(Base1, Base2):
#     def __init__(self, a, b, c):
#         Base1.__init__(self, a)
#         Base2.__init__(self, b)
#         self.c = c

# obj = Derived(10, 20, 30)

# print("a =", obj.a)
# print("b =", obj.b)
# print("c =", obj.c)




# ### Assignment 13: Checking Instance Types with Inheritance
# Create a base class named `Animal` and a derived class named `Cat`. Create objects of both classes and use the `isinstance` 
# function to check the instance types.

# class Animal:
#     pass

# class Cat(Animal):
#     pass

# # Create objects
# animal = Animal()
# cat = Cat()

# # Check instance types
# print(isinstance(animal, Animal))
# print(isinstance(cat, Cat))
# print(isinstance(cat, Animal))
# print(isinstance(animal, Cat))

# ### Assignment 14: Polymorphism with Inheritance
# Create a base class named `Bird` with a method `speak`. Create two derived classes `Parrot` and `Penguin` that override the 
# `speak` method. Create a list of `Bird` objects and call the `speak` method on each object to demonstrate polymorphism.


class Bird:
    def speak(self):
        print("Bird makes a sound.")

class Parrot(Bird):
    def speak(self):
        print("Parrot says: Hello!")

class Penguin(Bird):
    def speak(self):
        print("Penguin says: Honk!")

# List of Bird objects
birds = [Parrot(), Penguin()]

# Demonstrate polymorphism
for bird in birds:
    bird.speak()



# ### Assignment 15: Combining Single and Multiple Inheritance
# Create a base class named `Device` with an attribute `brand`. Create a derived class `Phone` that inherits from `Device` 
# and adds an attribute `model`. Create another base class `Camera` with an attribute `resolution`. Create a derived class 
# `Smartphone` that inherits from both `Phone` and `Camera`. Create an object of the `Smartphone` class and print its attributes.





class Device:
    def __init__(self, brand):
        self.brand = brand

class Phone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class Camera:
    def __init__(self, resolution):
        self.resolution = resolution

class Smartphone(Phone, Camera):
    def __init__(self, brand, model, resolution):
        Phone.__init__(self, brand, model)
        Camera.__init__(self, resolution)

# Create object
phone = Smartphone("Samsung", "Galaxy S24", "50 MP")

# Print attributes
print("Brand:", phone.brand)
print("Model:", phone.model)
print("Resolution:", phone.resolution)