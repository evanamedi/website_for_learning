# A class is a blueprint or prototype the defines the variables and the methods (functions) 
# common to all objects of a certain kind.

# An example of a class in Python would be:

class Car:
	def __init__(self, brand, model, year):
		self.brand = brand
		self.model = model
		self.year = year

	def start_engine(self):
		print("Engine Started")

# In this example, [ Car ] is the class. It has an __init__ method that is used to initialize
# new objects of this class, and a [ start_engine ] method that all [ Car ] objects will have.


# An object is an instance of a class. It has real values instead of variables
# you can create an object of the [ Car ] class like so:

my_car = Car("Toyota", "Supra", 2021)

# In this example, [ my_car ] is an object of the [ Car ] class, with brand "Toyota", 
# model "Corolla", and year 2021. You can call the methods of the class on this object like this:

my_car.start_engine()	# prints "Engine started"


# Each object has its own values for the variables defined in the class, and can use the methods
# defined in the class. You can create as many objects of a class as you need, and they are all
# independent of each other. If you change a variable in one object, it does not affect
# other objects.

# In summary, a class is like a blueprint, and an object is something you build based on
# that blueprint. The class defines what variables and methods an object will have, and
# the object is an instance of the class with actual values.


# Benefits of using classes and objects in OOP:

# Modularity:
# The source code for an object can be written and maintained independently of the source
# code for other objects. Once created, an object can be easily passed around inside the system.

# Information-hiding:
# By interacting only with an object's methods, the details of its internal implementation
# remain hidden from the outside world.

# Code Re-usability:
# If an object already exists (perhaps written by another person), you can use that object
# in your program. This allows specialists to implement/test/debug complex, task-specific
# objects, which you can then trust to run your own code.

# Pluggability & Debugging Ease:
# If a particular object turns out to be problematic, you can simply remove it from your
# application and plug in a different object as its replacement. This is analogous to fixing
# mechanical problems in the real world. If a bolt breaks, you replace it, not the entire machine.

# Encapsulation:
# A class or object can encapsulate functionality and data into one reusable package. the data
# (attributes) and code (methods) are tied together as a self-contained unit called an object.
# This encapsulation helps manage complexity by keeping the interactions between objects under
# control.

# Inheritance:
# Classes can inherit common properties and functionality from other classes. This allows for
# more efficient and consistent code by allowing classes to share, extend, and override 
# configurations and behaviors defined in other classes.

# Polymorphism:
# Polymorphism allows a single interface to represent different types of objects at runtime.
# This means that different classes can define the same method or property and you can use
# objects of different classes interchangeably.



# These benefits make OOP a popular choice for large, complex software systems and applications
# where ease of maintenance, rapid development, and code reusebility are important.

















#_______________________