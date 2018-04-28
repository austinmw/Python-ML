while True:
	try:
		number = int(input("Enter a number: "))
		print(5/number)
		break
	except ValueError:
		print("Bad value")
	except ZeroDivisionError:
		print("Don't pick zero")
	except: # general exception
		print("some other error")
		break
	finally: #optional, execute no matter what (either try or except)
		print("Loop complete")