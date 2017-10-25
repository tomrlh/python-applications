def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f

temperatures = [10, -20, -289, 100]
file_name = "example3.txt"
file = open(file_name, "r+")

for temp in temperatures:
	file.write(str(c_to_f(temp)) + "\n")

file.close()