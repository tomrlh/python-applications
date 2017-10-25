# Handling errors

def divide(a, b):
	try:
		return a / b
	except Exception as e:
		return("You cant divide a number by 0")


print(divide(1, 0))