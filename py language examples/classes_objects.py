class MyStuff(object):

	def __init__(self): # not required, but automatically called when object created
		self.tangerine = "And now a thousand years between"

	def apple(self):
		print("I AM CLASSY APPLES!")
		
		
thing = MyStuff()
thing.apple()
print(thing.tangerine)


# -----------------------

class Enemy:
	def __init__(self, x):
		self.energy = x
		
	def get_energy(self):
		print(self.energy)

jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()

# --------------------

class Girl:
	gender = "female" # class variable, shared between all objects
	
	def __init__(self, name):
		self.name = name        # instance variable, unique
		
r = Girl("rachel")
s = Girl("susan")
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)		