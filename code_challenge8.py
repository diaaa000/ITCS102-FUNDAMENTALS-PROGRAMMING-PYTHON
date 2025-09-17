#MULTIPLICATION TABLE

an = int(input("Enter a number: --> "))

print(f"Multiplication Table for {an}: ")

for y in range(1,11):
	result = an * y
	print(f"{an} × {y} = {result}")
