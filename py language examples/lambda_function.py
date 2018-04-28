# lambda functions have no name, are one time use
# use lambdas when you don't need to reuse a function

# e.g.: Button(text="Click Me", command=lambda:custom_functionality)
# command=function, but don't need to create separate function

answer = lambda x: x*7  # input : what to do

print(answer(5))
	

