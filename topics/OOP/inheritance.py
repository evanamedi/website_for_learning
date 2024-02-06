# Inheritance is a fundamental principle of OOP that allows one class to inherit properties
# and methods from another class. It promotes the concept of reusability and is a way to create
# a new class using properties of an existing class without modifying it.

# Key Concepts:

# Base Class (Parent Class):
# The class whose properties and methods are inherited is known as the base case or parent class

# Derived Class (Child Class):
# The class that inherits properties from another class is known as the derived class
# or child class

# Inheritance Types:
# There are several types of inheritance, including single, multiple, multilevel, hierarchical,
# and hybrid inheritance. The type of inheritance implemented depends on the programming
# language used.

# Method Overriding:
# In the derived classes, you can modify the behavior of methods inherited from the base class.
# This is known as method overriding

# Access Modifiers:
# These define the accessibility of the properties and methods of a class. Common access
# modifiers include public, private, and protected.


# Example of inheritance in Python:

class Animal:	# Base class
	def __init__(self, name):
		self.name = name

	def speak(self):
		pass	# To be defined by subclass

class Dog(Animal):	# Derived class
	def speak(self):
		return "woof!"

class Cat(Animal):	# Derived class
	def speak(self):
		return "Meow!"

# In this example, [ Dog ] and [ Cat ] classes inherit from the Animal class. Both [ Dog ] and
# [ Cat ] override the [ speak ] method of Animal. Now, if you create instance of [ Dog ] and [ Cat ]
# you can call the [ Speak ] method on them:

fido = Dog("Fido")
print(fido.speak())		# prints "Woof!"

whiskers = Cat("Whiskers")
print(whiskers.speak())		# prints "Meow!"


# Inheritance allows for more organized and manageable code, making it easier to create and
# maintain applications. The derived classes have their own methods and can also use the
# methods of the base class, reducing code duplication.



# More Examples:



# Example 1 (using the super() function):

# The [ super() ] function in Python is used in the child class to refer to the parent class
# without explicitly naming it. It's useful especially in cases of multiple inheritance where
# you want to avoid naming the parent class explicitly.

class Mammal:
	def __init__(self, mammalName):
		print(mammalName, " is a warm-blooded animal.")

class Dog(Mammal):
	def __init__(self):
		print("Dog has four legs.")
		super().__init__("Dog")

d1 = Dog()

# The output would be:
# "Dog has four legs."
# "Dog is a warm-blooded animal."

# Breakdown:
# When d1 = Dog() is executed, it called the __init__ method in the dog class
# The Dog class's __init__ method first prints "Dog has four legs."
# Then, super().__init__("Dog") is called. This calls the __init__ method of the Mammal class
# (the parent class), passing "Dog" as an argument
# The mammal class's __init__ method prints "Dog is a warm-blooded animal."




# Example 2 (Multiple Inheritance):
# Python supports multiple inheritance, where a class can be derived from more than one
# base classes.

class Animal:
	def eats(self):
		return "Eats food"

class Bird:
	def flies(self):
		return "Flies in the sky"

class Sparrow(Animal, Bird):
	pass

s = Sparrow()
print(s.eats())		# prints "Eats food"
print(s.files())	# prints "Flies in the sky"

# In this example, [ Sparrow ] is derived from both [ Animal ] and [ Bird ] classes,
# and inherits methods from both.




# Example 3 (Method Overriding):
# In Python, method overriding occurs by simply defining in the child class a method with
# the same name of a method in the parent class.

class Bird:
	def intro(self):
		print("There are many types of birds.")

	def flight(self):
		print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
	def flight(self):
		print("Sparrows can fly.")

class ostrich(Bird):
	def flight(self):
		print("Ostriches cannot fly.")

b1 = Bird()		
b2 = sparrow()	
b3 = ostrich()	

b1.intro()	# "There are many types of birds."
b1.flight()	# "Most of the birds can fly but some cannot."

b2.intro()	# "There are many types of birds."
b2.flight()	# "Sparrows can fly."

b3.intro()	# "There are many types of birds."
b3.flight()	# "Ostriches cannot fly."

# In this example, sparrow and ostrich classes override the flight method of the bird class

# When [ b1.intro() ] and [ b1.flight() ] are called, it prints "There are many types of
# birds." and "Most of the birds can fly but come cannot." because [ b1 ] is an instance
# of the [ Bird ] class

# When [ b2.intro ] and [ b1.flgiht ] are called, it prints "There are many types of birds."
# and "Sparrows can fly." because b2 is an instance of the sparrow class. The [ intro() ]
# method is inherited from the [ Bird ] class and the [ flight() ] method is overridden in
# the [ sparrow ] class.

# When [ b3.into() ] and [ b3.flight() ] are called, it prints "There are many types of birds."
# and "Ostriches cannot fly." because [ b3 ] is an instance of the [ ostrich ] class. The
# [ intro() ] method is inherited from the [ Bird ] class and the [ flight() ] method is 
# overridden in the [ ostrich ] class.











#_______________________