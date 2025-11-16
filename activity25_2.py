
#functions with parameters

def factorial(num):
	fact = 1
	for x in range(num, 0 , -1):
		fact *= x
	return fact
	
def some_triangle(num):
	for i in range(1, int(num) + 1, 1):
		#for y in range(1, i, 1):
		#	print(" ", end= ' ')
		for z in range(10, i, -1):
			print("*", end= " ")
		print()
		
	
