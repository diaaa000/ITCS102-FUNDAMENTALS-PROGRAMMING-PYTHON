#FACTORIAL PROGRAM

an = eval(input("Enter a number : --> "))

result = 1
for y in range (an, 0, -1):
	print(result, "*", y, " = ", result)
	result *= y 

print("Factorial is", result)
