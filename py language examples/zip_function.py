# zip two lists of equal length together into a tuple

first = ['Bucky', 'Tom', 'John']
last = ['Roberts', 'Hanks', 'Wayne']

names = zip(first, last)  # makes a list of tuples

for a, b in names:
	print(a, b)
	
	
	