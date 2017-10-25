# Writing Multiple Lines in a Text File

file_name = "example2.txt"

file = open(file_name, "w")
numbers = [1, 2, 3]

for i in numbers:
	file.write(str(i) + "\n")

file.close()