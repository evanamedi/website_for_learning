# Abstraction is the process of hiding the complex details of an operation while providing
# a simpler interface.


# Data Abstraction:
# Data abstraction is about providing only essential information to the outside world while hiding
# their background details, i.e., how the data is stored and operations are performed. In
# other words, the user interacts with only the information that is necessary, while the
# underlying complexities and hidden from the user.

# Method Abstraction:
# This is achieved by creating methods that perform complex operations, but providing a simple
# interface for them. The user doesn't need to know how the method does what it does- they just
# need to know what it does.

# Abstract Classes and Methods:
# In some programming languages like Java & C#, you can create abstract classes and methods.
# An abstract class is a class that cannot be instantiated and is meant to be subclassed. It
# can contain abstract methods (methods declared without an implementation) as well as 
# concrete methods (methods with an implementation). Subclasses of an abstract class are generally
# expected to provide an implementation for the abstract methods.

# Interface:
# An interface is a completely abstract class that contains only abstract methods. In languages
# that support interfaces, they are a powerful way to achieve full abstraction and 
# multiple inheritance.

# Encapsulation and Information Hiding:
# Abstraction is closely related to encapsulation and information hiding. Encapsulation is the
# bundling of data and methods that operate on that data within one unit, and information 
# hiding is about making the data inaccessible to the outside world. Abstraction takes this
# a step further by not only hiding the data, but also by hiding how the methods of a
# class are implemented.


# The main advantage of abstraction is that it reduces complexity by breaking down complex
# systems into smaller, more manageable parts. This is also increases the maintainability,
# reusability, and modularity of the code. It allows you to change the implementation of 
# an abstracted operation without affecting the rest of the code, as long as the interface
# stays the same.


# Consider an example of a payment processing system. In this system, we have different
# payment methods like Credit Card, Debit Card, and PayPal. Each payment method follows
# the same process: authorize the payment and then charge the payment. However, the
# implementation details for each payment method are different.

# In Python:

from abc import ABC, abstractmethod

class PaymentMethod(ABC):	# define an abstract base class- PaymentMethod
	@abstractmethod		# declare an abstract method- authorize
	def authorize(self):
		pass

	@abstractmethod		# declare and abstract method- charge
	def charge(self):
		pass

class CreditCard(PaymentMethod):	# define a concrete class- CreditCard, that inherits from PaymentMethod
	def authorize(self):	# provide and implementation for the- authorize method
		print("Authorizing Credit Card")

	def charge(self):	# provide an implementation for the- charge method
		print("Charging Credit Card")

class PayPal(PaymentMethod):	# define a concrete class- PayPal that inherits from PaymentMethod
	def authorize(self):	# provide an implementation for the- authorize method
		print("Authorizing PayPal Account")

	def charge(self):	# provide an implementation for the- charge method
		print("Charging PayPal Account")

class PaymentProcessor:		# define a class- PaymentProcessor
	def process_payment(self, payment_method):		# Define a method- process_payment that takes a PaymentMethod object
		payment_method.authorize()	# call the- authorize method on the PaymentMethod object
		payment_method.charge()		# class the- charge method on the- PaymentMethod object

payment_processor = PaymentProcessor()

credit_card = CreditCard()	# create a PaymentProcessor object
payment_processor.process_payment(credit_card)	# use the PaymentProcessor to process the payment with the- CreditCard

paypal = PayPal()	# create a PayPal object
payment_processor.process_payment(paypal)	# use the PaymentProcessor to process the payment with PayPal

# In this code, [ PaymentMethod ] is an abstract base class that declares two abstract
# methods: [ authorize ] and [ charge ]. [ CreditCard ] and [ PayPay ] are concrete classes
# that inherit from [ PaymentMethod ] and provide their own implementations of these methods.

# The [ PaymentProcessor ] class has a [ process_payment ] method that takes a [ PaymentMethod ]
# object and calls its [ authorize ] and [ charge ] methods. This method doesn't need to know
# what specific type [ PaymentMethod ] it's dealing with, it just knows that it can call
# [ authorize ] and [ charge ] on it. This is abstraction in action.


# More detailed explanation:

# In the system, [ PaymentMethod ] is an abstract base class (ABC) that defines a common
# interface for all payment methods. This interface includes two methods: [ authorize ]
# and [ charge ]. These methods are marked as abstract, meaning they have no implementation
# in [ PaymentMethod ] and must be implemented by any concrete (i.e., non-abstract) subclass.

# [ CreditCard ] and [ PayPal ] are concrete classes that inherit from [ PaymentMethod ] and
# provide their own implementations of the [ authorize ] and [ charge ] methods. These
# implementations contain the specific steps required to authorize and charge a payment using
# each method.

# The [ PaymentProcessor ] class represents the part of the system that processes payments. It
# has a [ process_payment ] method that takes an object of type [ PaymentMethod ] and called its
# [ authorize ] and [ charge ] methods. This method doesn't need to know the details of how each
# payment method authorized and charges payments; it just needs to know that it can call
# [ authorize ] and [ charge ] on any [ PaymentMethod ] object.

# This is where the power of abstraction comes in. By defining a common interface for all
# payment methods, we can write code in [ PaymentProcessor ] that works with any payment method,
# regardless of its specific implementation. This makes [ PaymentProcessor ] more flexible
# and easier to maintain. If we want to add a new payment method in the future, we just need
# to create a new class that implements the [ PaymentMethod ] interface; we don't need to
# change any code in [ PaymentProcessor ].

# Abstraction in this context is used to hide the complex details of authorizing and charging
# different types of payments, while providing a simple, consistent interface for processing
# any type of payment. This reduces complexity, improves maintainability, and makes the code
# more flexible and extensible.
















#_______________________________