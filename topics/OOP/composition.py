# Composition is a design principle in OOP where a class (the "composite" or "parent") is made
# up of other classes (the "components" or "children"). It represents a "part-of" relationship
# and is a strong form of aggregation. 


# Key points:


# Definition:
# Composition is a relationship where one class (The composite) contains an instance of 
# another class (the component). The component is part of the composite. For example, a Car
# might have an Engine. The car is the whole entity, and the engine is part of the car.

# Dependence:
# In a composition relationship, the component cannot exist independently of the composite.
# If the composite is deleted, the component is also deleted. For example, if you deleted
# a Car object, the Engine object is also deleted because it's part of the car.

# Lifecycle:
# The lifecycle of the component is managed by the composite. the component is created when
# the composite is created, and deleted when the composite is deleted.

# Direction:
# Composition is typically and one-way relationship. The composite knows about the 
# component, but the component does not know about the composite.

# Python example:

class Engine:
	def __init__(self, type):
		self.type = type

class Car:
	def __init__(self, model, engine_type):
		self.model = model
		self.engine - Engine(engine_type) # the Car creates an Engine

# create a Car instance with an Engine
car = Car("Toyota", "V8")

# In this example, the [ Car ] class has a composition relationship with the [ Engine ] class.
# The [ Car ] creates an [ Engine ] when it's created, so the [ Engine ] is part of the 
# [ Car ] and can't exist independently.






# The Difference Between This Example and the Example Dealing with Aggregation:

# The key difference between the two examples lies in the lifecycle and dependency of the 
# [ Engine ] object with respect to the [ Car ] object.



# In Aggregation:

class Engine:
	def __init__(self, type):
		self.type = type

class Car:
	def __init__(self, model, engine):
		self.model = model
		self.engine = engine # the Car has an Engine

# create an Engine instance
engine = Engine("V8")

# create a Car instance with the Engine
car = Car("Toyota", engine)

# The engine instance is created independently of the [ Car ] instance. The [ Car ] instance
# then takes an existing [ Engine ] instance as a parameter. This means the [ Engine ] can
# exist without the [ Car ], and if the [ Car ] is deleted, the [ Engine ] continues to exist.
# This is a characteristic of aggregation.



# In Composition:

class Engine:
	def __init__(self, type):
		self.type = type

class Car:
	def __init__(self, model, engine_type):
		self.model = model
		self.engine = Engine(engine_type) # the Car creates and Engine

# create a Car instance with an Engine
car = Car("Toyota", "V8")

# The [ Car ] instance creates its own [ Engine ] instance when it's constructed. The
# instance cannot exist without the [ Car ] instance, and if the [ Car ] is deleted,
# the [ Engine ] is also deleted. This is a characteristic of composition.



# So, the main difference is about the dependency and lifecycle of the [ Engine ] with
# respect to the [ Car ]. In aggregation, the [ Engine ] can exist independently, while
# in composition, the [ Engine ] is fully dependent on the [ Car ].














#_______________________________