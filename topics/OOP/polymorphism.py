# The word "Polymorphism" comes from Greek and means "many shapes". In programming, it refers
# to the ability of an object to take on many forms. The most common use of polymorphism in OOP
# occurs when a parent class reference is used to refer to a child class object.

# Breakdown:

# Subtyping:
# Subtyping, also known as subtype polymorphism, is a form of polymorphism in which a subclass
# is a datatype that is a subtype of a superclass. The superclass can be used to refer to the
# subclass object. In other words, a reference variable of a superclass can point to an 
# object of the subclass

# Method Overriding:
# Method overriding is a feature that allows a subclass to provide a different implementation for
# a method that is already defined in its superclass. This is used to achieve runtime polymorphism

# Operator Overloading:
# Operator overloading is a type of polymorphism in which an operator is overloaded to provide
# the special meaning to the user-defined data type. Operator overloading is used to perform
# operations on user-defined data type like complex numbers, fractions, etc.


# Example of polymorphism in Python (also previously used to demonstrate inheritance):

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

bird1 = Bird()
bird2 = sparrow()
bird3 = ostrich()

bird1.intro()	# "There are many types of birds."
bird1.flight()	# "Most of the birds can fly but some cannot."

bird2.intro()	# "There are many types of birds."
bird2.flight()	# "Sparrows can fly."

bird3.intro()	# "There are many types of birds."
bird3.flgiht()	# "Ostriches cannot fly."

# In the above program, we defined two classes [ sparrow ] and [ ostrich ], both are subclasses
# of [ Bird ]. A method named [ flight ] is created in [ Bird ] class and overridden in both
# subclasses. This is a perfect example of polymorphism as the method [ flight ] is taking
# multiple forms.

# polymorphism allows us to define methods in the child class with the same name as defined
# in their parent class. As the key aspect of polymorphism is that it provides flexibility and
# loose coupling so that code can be extended and easily maintained over time.



# The previous explanation focused on inheritance. Inheritance is a mechanism where you can
# derive a class from another class for a hierarchy of classes that share a set of attributes
# and methods. In the example, [ sparrow ] and [ ostrich ] classes are derived from the [ Bird ]
# class, hence they inherit the intro method from the [ Bird ] class.

# The current explanation focuses on polymorphism, which is a concept that allows objects of
# different classes to be treated as objects of a superclass. In the context of the example,
# both [ sparrow ] and [ ostrich ] classes override the [ flight ] method of the [ Bird ]
# class. When we call the [ flight ] method on an object of type [ Bird ], [ sparrow ],
# or [ ostrich ], the appropriate version of the method is executed based on the actual type
# of the object. This is polymorphism in action.





# Further Explanation:

# Inheritance:
# is the mechanism where a class (the subclass) can derive or inherit properties and methods
# from another class (the superclass). In the given example, [ sparrow ] and [ ostrich ] are
# subclasses that inherit from the [ Bird ] superclass, and this they inherit the [ into ]
# and [ flight ] methods

# Polymorphism:
# on the other hand, is the ability of the subclasses to provide their own specific 
# implementation of a method that is already provided by their superclass. In the example,
# the [ sparrow ] and the [ ostrich ] subclasses provide their own implementation of the flight
# method. This is a from of polymorphism known as method overriding.

# So, when a method is invoked, which version of the method is to be executed is determined
# based on the type of object being invoked on. If it's a [ Bird ] object, [ Bird ]s version
# of [ flight ] is called. If it's a [ sparrow ]. or [ ostrich ] object, their respective
# version of [ flight ] are called. This ability to "take many forms" is the essence of 
# polymorphism.




# Common use cases:

# Creating Reusable Code:
# Polymorphism allows you to write code that does not need to be changed when a new derived
# class is added, which makes your code more reusable. You can write a function or method
# that uses a base class type and it will be able to handle any objects of classes derived
# from that base class.

# Implementing Interface Polymorphism:
# In languages that support interfaces (like Java or C#), polymorphism is often used to
# implement classes that share the same methods but have different implementations. This is
# a powerful way to decouple your code and make it more modular and flexible.

# Design Patterns:
# Many design patterns in OOP use polymorphism. For example, in the Strategy pattern, a context
# object contains a reference to a strategy object, and delegates all requests to that object.
# The strategy object can be changed to change the behavior of the context object.

# Abstract Classes and Methods:
# In some languages, you can define abstract classes and methods that provide a base level
# of functionality, but require subclasses to provide specific implementations. This is a
# form of polymorphism.

# Graphics and User Interface:
# In graphical and user interface programming, polymorphism is used extensively. For example,
# you might have a base [ Shape ] class and derived classes like [ Circle ], [ Rectangle ], etc.
# You can then write code that works with [ Shape ] objects, and it will work with any
# derived shape objects.

# Game programming:
# In game programming, polymorphism is used to manage and manipulate collections of different
# types of game objects. For example, you might have a base [ GameObject ] class and derived
# classes like [ Player ], [ Alien ], [ Asteroid ], etc.


# The main benefit of polymorphism is that it allows you to write more flexible and reusable
# code by allowing objects of different classes to be treated as objects of a common superclass.



















#________________________________