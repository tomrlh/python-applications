def celsius_to_fahrenheit(temperature):
	return temperature * 9 / 5 + 32

print(celsius_to_fahrenheit(40))



def celsius_to_fahrenheit_modified(temperature):
	print(temperature)
	if -273 <= temperature:
		return temperature * 9 / 5 + 32
	else:
		return "The lowest temperature supported is -273.15 ºC"


print(celsius_to_fahrenheit_modified(-273))
