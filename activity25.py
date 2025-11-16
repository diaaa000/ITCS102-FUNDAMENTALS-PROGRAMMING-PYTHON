
from activity25_1 import *
from activity25_2 import *

#Creating a Menu Options with While loop and functions

name = input("Hi, What is your name ---> ")

print(f"Welcome  {name}, to my Compiler Program ")

isContinue = True

while isContinue == True:
	print("Select a Program")
	print("A - Activity1\nB - Activity2\nC - Activity15\nD - Factorial\nF - Triangle\nE - Exit")
	
	choose = input("What program / code would you like to run ---> ").lower()
	
	if choose == 'a':
		activity1()
		continue 
	elif choose == 'b':
		activity2()
		continue
	elif choose == 'c':
		add_odd()
		continue
	elif choose == 'd':
		print("Factorial Program")
		num = input("Input a number for factorial computation --->")
		print(f"The factorial of {num} is {factorial(num)}")
		continue
		
	elif choose == 'f':
		some_triangle()
		continue
	elif choose == 'e':
		print("System Exit")
		break
	else:
		print("Invalid Choice")
		
	
	
	
