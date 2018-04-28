xfrom operator import attrgetter

# create User class
class User:
	def __init__(self, x, y):
		self.name = x
		self.user_id = y
		
	def __repr__(self):   # representation of this object
		return self.name + ":" + str(self.user_id)
	
# create list of User objects		
users = [
	User('Bucky', 43),
	User('Sally', 5),
	User('Tuna', 61),
	User('Brian', 2),
	User('Joby', 77),
	User('Amanda', 9)	
]		

# test print (default order)
for user in users:
	print(user)
	
# sort by name	
print('-------')
for user in sorted(users, key=attrgetter('name')):
	print(user)
	

# sort by id	
print('-------')
for user in sorted(users, key=attrgetter('user_id')):
	print(user)
	
	
	
