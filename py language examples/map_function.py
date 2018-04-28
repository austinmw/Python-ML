# map function is a way to take a list and run each item through a function

income = [10, 30, 75]

def double_money(dollars):
	return dollars * 2
	
# map(function to run items through, list to iterate through)	
new_income = list(map(double_money, income)) # put each in a list (or could do a for loop)
print(new_income)