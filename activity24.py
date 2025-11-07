def greeter(name):
	print(f"Haro, {name}, have a great day!")
	
def summation(y):
	sum = 0
	for x in range(y, 0, -1):
		sum += x
	print(f"The sum of {y} is {sum}")
	
summation(5)
summation(10)
summation(15)

#greeter("dia")
#greeter("yannie")
#greeter("diane")
