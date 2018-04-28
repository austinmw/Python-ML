# https://blog.dbrgn.ch/2013/3/26/perceptrons-in-python/

# OR perceptron

# import libraries
from random import choice 
from numpy import array, dot, random 

# step function
unit_step = lambda x: 0 if x < 0 else 1 

# map possible input to expected output
# OR, AND, NOR, NOT will work
# XOR won't work using single perceptron because the two classes (0 and 1) are not linearly seperable
training_data = [ (array([0,0,1]), 0), (array([0,1,1]), 1), (array([1,0,1]), 1), (array([1,1,1]), 1) ] 


# random initial weights
w = random.rand(3) 

# initialize variables 
errors = [] # store error values to plot later
eta = 0.2 # learning rate
n = 100  # number of learning iterations

# train the perceptron
for i in range(n): 
	x, expected = choice(training_data) 
	result = dot(w, x) 
	error = expected - unit_step(result) 
	errors.append(error) 
	w += eta * error * x 
	
print(w, '\n')	
	
for x, _ in training_data: 
	result = dot(x, w) 
	print("{}: {} -> {}".format(x[:2], result, unit_step(result)))



from pylab import plot, ylim 
ylim([-1,1]) 
plot(errors)
