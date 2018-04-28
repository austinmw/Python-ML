# Basic example

class This_is_a_very_long_class_name(object):
	def __init__(self):
		pass
 
class Derived(This_is_a_very_long_class_name):
	def __init__(self):
		super().__init__()   #1
		This_is_a_very_long_class_name.__init__(self)    #2		
		# Both 1 and 2 do the same thing, but 1 is a lot easier		
		
	
	
	
# Multiple inheritance example	
		
class A(object):
	def foo(self):
		print('A')
 
class B(A):
	def foo(self):
		print('B')
		super().foo()
 
class C(A):
	def foo(self):
		print('C')
		super().foo()
 
class D(B,C):
	def foo(self):
		print('D')
		super().foo()
 
d = D()
d.foo()		