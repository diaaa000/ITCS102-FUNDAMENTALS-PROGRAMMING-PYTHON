odd_sum = 0

for y in range(1,11,1):
	an = eval(input(f"{y} - Enter a number ---> "))
	if an %2 == 1:
		odd_sum += an
		
print(f"The sum of all the ODD numbers given is {odd_sum}")
