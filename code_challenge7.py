#summation of odd numbers
#loop 10 times

sum_of_odd = 0
for y in range(10):
	n = int(input(f"Enter a number: "))
	if n % 2 != 0:
		sum_of_odd += n
		
		
print("The sum of all the odd numbers is", sum_of_odd)
