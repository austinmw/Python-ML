def health_calculator(age, apples_ate, cigs_smoked):
	answer = (100-age) + (apples_ate * 2.5) - (cigs_smoked * 3)
	print(answer)
	
my_data = [26, 1, 0]

# Unpacking an argument list
health_calculator(*my_data)