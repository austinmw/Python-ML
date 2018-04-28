# assigning to an instance attribute needs to know what instance to assign to, and that's why it needs self.
# the first parameter of methods is the instance the method is called on

class Parent:						# parenthesis are optional when defining a class
	def print_last_name(self):
		print('Welch')
		
class Child(Parent):   # Inherit Parent class
	def print_first_name(self):
		print('Austin')
		
# If you create a print_last_name function in Child class, it will replace the inherited function of the same name		
		
me = Child()
me.print_first_name()
me.print_last_name()		


