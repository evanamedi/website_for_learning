# Encapsulation is one the fundamental concepts in OOP. It describes the idea of wrapping data and
# the methods that work on data within one unit. This puts restrictions on accessing variables
# and methods directly and can prevent the accidental modification of data.

# Breaking it down:


# Data Hiding:
# The implementation of the class is hidden from other classes, and can only be accessed
# through the methods of their current class. This is also known as data hiding.

# Accessors and Mutators: 
# To achieve encapsulation in Python, you can use private attributes and provide public getter
# and setter methods to modify and access the attributes. These are often referred to as
# accessors (getters) and mutators (setters).

# Abstraction:
# Encapsulation also allows a class to change its implementation without affecting other parts
# of the code, which is known as abstraction. 


# Example in Python:

class Computer:		# define a class named Computer

	def __init__(self):		# initialize method or constructor for the class
		self.__maxprice = 900	# private attribute, not directly accessible from outside the class

	def sell(self):		# public method to print the selling price
		print("Selling Price: {}".format(self.__maxprice))

	def setMaxPrice(self, price):	# public method (setter) to set the price of the computer
		self.__maxprice = price 	# modifying the private attribute within the class

c = Computer()	# create an object of the computer class
c.sell()	# call the sell method, it will print the initial price

c.__maxprice = 1000		# try to directly change the price
c.sell()	# call the sell method, it will still print the initial price because we can't
																		# change it directly
# using setter function		# use the setter method to change the price
c.setMaxPrice(1000)		# now, when we call the sell method, it will print the updated price
c.sell()

# In the script we defined a [ Computer ] class.
# We are using [ __init__() ] method to store the maximum selling price of [ Computer ]. We
# tried to modify the price. However, we can't change it because Python treats the
# [ __maxprice ] as private attributes.

# As a result, to change the value, you have to use a setter method [ setMaxPrice() ] which
# takes price as parameter.

# The output would be:
# Selling Price: 900
# Selling Price: 900
# Selling Price: 1000

# Encapsulation helps us to avoid data being modified accidentally and provides a way to 
# protect and control access to attributes in a class

# Another way to sum it up again:
# the [ Computer ] class encapsulates the [ __maxprice ] attribute and provides the [ sell ]
# method to display it, and the [ setMaxPrice ] method to change it. The [ __maxprice ]
# attribute is not directly accessible from outside the class - trying to change it directly
# won't have any effect. Instead, you have to use the [ setMaxPrice ] method to modify it.



# Another Example:

# A setter method provides controlled access to modify the values of private attributes. This
# is useful because you can add checks or validation within the setter method to prevent
# invalid or inconsistent states for your objects

class Myclass:
	def __init__(self):
		self.__my_attribute = 0

	def set_my_attribute(self, value):
		if value < 0:
			raise ValueError("Value cannot be negative")
		self.__my_attribute = value

obj = Myclass()
obj.set_my_attribute(10)	# this modifies the __my_attribute value to 10

# In this example, [ set_my_attribute ] is a setter method that modifies the value of
# [ __my_attribute ]. It also includes a check to ensure that the value cannot be set
# to a negative number. If you try to set it to a negative number, it will raise a ValueError





# Some Best Practices For Using Encapsulation In OOP:

# Data Hiding:
# Keep the data hidden and not directly accessible from outside the class. Use private visibility
# for attributes which should no be accessible directly.

# Use Accessors and Mutators:
# Provide public getting and setter methods (accessors and mutators) to access and modify the
# private attributes of a class. This allows you to control how important variables are read
# and written to.

# Validation:
# You can add validation logic in setter methods to protect your data from getting into an
# inconsistent or invalid state.

# Abstraction:
# Encapsulation is a way to achieve data abstraction. The user will have the information
# on what methods do, but they won't need to know how they do it.

# Reduce Coupling:
# Encapsulation can help reduce coupling between different parts of your program, making it
# easier to modify without affecting other parts of the code.

# Consistency:
# Be consistent in how you apply encapsulation in your code. If you start using getters
# and setters for accessing properties of the class, stick to it throughout your code.

# Avoid Excessive Use:
# While encapsulation is important, it's also crucial not to overuse it. Not every single
# variable needs to be private with getters and setters. If a variable doesn't need any
# special behavior or constraints, it might not need to be encapsulated. 











#___________________________________

