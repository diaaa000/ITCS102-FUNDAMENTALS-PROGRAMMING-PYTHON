
#activities

def activity1():
	x = 5
	print("The value of x is ", x)
	
def activity2():
	name = input("What is your name?")
	print("Hi", name , "Welcome to the game")
	
def add_odd():
	odd_sum = 0
	for i in range(1, 11, 1):
		num = eval(input(f"{i} - Enter a number --> "))
		
		if num % 2 == 1:
			odd_sum += num
			
		print(f"The sum of all the ODD numbers given is {odd_sum}")
		

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
	       print(f"{an} × {y} = {result}")
