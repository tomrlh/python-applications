def string_length(string):
	return len(string)

print(string_length("test"))


def string_length_modified(mystring):
	if type(mystring) == int:
		return "Sorry integers don't have length"
	elif type(mystring) = float:
		return "Sorry float numbers don't have length"
	else:
		return len(mystring)

print(string_length_modified(10))