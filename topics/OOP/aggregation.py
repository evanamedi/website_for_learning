# Aggregation is a special form of association in OOP. It represents a "has-as"" relationship
# between two classes, where one class is a complex entity that consists of one or more other
# classes, but there is still independence of the classes.

# Key Points:


# Definition:
# Aggregation is a relationship where one class (the "whole" or "parent") has a reference to 
# another class (the "part" or "child"), but the child can exist independently of the parent.
# For example, a Car might have an Engine. The car is the whole entity that uses the engine,
# but the engine could exist without the car.

# Independence:
# In an aggregation relationship, the child can exist independently of the parent. If the
# parent is deleted, the child can continue to exist. For example, if you delete a Car
# object, the Engine object can still exist.

# Lifecycle:
# The lifecycle of the child is not managed by the parent. The child can be created and
# deleted independently.

# Direction:
# Aggregation is typically a one-way relationship. The parent knows about the child, but the
# child does not know about the parent.

# Example:

class Engine:
	def __init__(self, type):
		self.type = type

class Car:
	def __init__(self, model, engine):
		self.model = model
		self.engine = engine	# the Car has an Engine

# create an Engine instance
engine = Engine("V8")

# create a Car instance with Engine
car = Car("Toyota", engine)

# In this example, the [ Car ] class has an aggregation relationship with the [ Engine ]
# class. The [ Car ] has an [ Engine ], but the [ Engine ] can exist independently of the
# [ Car ].