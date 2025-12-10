
#code_challenges

def factorial():
	an = eval(input("Enter a number : --> "))
	result = 1
	
	for y in range (an, 0, -1):
	       print(result, "*", y, " = ", result)
	       result *= y 
	       
	print("Factorial is", result)
	
def multiplication():
	an = int(input("Enter a number: --> "))
	
	print(f"Multiplication Table for {an}: ")
	
	for y in range(1,11):
	       result = an * y
	       print(an,"x", "y", "=", result)

