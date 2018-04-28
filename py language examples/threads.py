# Threading: do multiple things at once
# Usage example: messanger program, i.e. sending & listening at the same time
# Good for programs with concurrency

import threading

class MyMessanger(threading.Thread): # inherit thread functions
	def run(self):  # run is special to threads, creating a thread will call run function
		for _ in range(10):  # convention for when you don't need to use the variable
			print(threading.currentThread().getName())

# Now multiple objects from this class can be threaded (ran at the same time)

x = MyMessanger(name='Send out msgs') # name is a default (optional) property of threads
y = MyMessanger(name='Receive msgs')

x.start()  # calls run function, moves to next line immediately (before finishing run)
y.start()