password = ""
correct_pswd = "python123"

while password != correct_pswd:
	password = input("Enter password: ")
	if(password == correct_pswd):
		print("You are logged in!")
	else:
		print("Sorry, try again!")