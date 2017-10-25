# Reading Files
file_name = 'fruits.txt'

file = open(file_name, "r")
content = file.readlines()
file.close()

for i in content:
	print(i.strip("\n"))



# Caulculating File Content Length-
for i in content:
	print(len(i) - 1)