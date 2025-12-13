#Activities

def activity1():
	name  = input("What is your name?")
	
	print("Haro,", name, "\nWelcome to the game")
	
def activity2():
	x = "Princess Diane Salumbides"
	print("X =", x)

def activity3():
	print("Happy\n\tFriday, ")
	print("\n\t\tBSIT 1A\n\t\t\tfrom DLL")        
	print("Princess\n\n\t\tDiane\n\n\t\t\t\tSalumbides")
	
def activity4():
	name = input("Enter a string --> ")
	
	print("Your name has ", len(name), "characters")

def activity5():
	something = eval(input("Input something --> "))
	print("The data type of something is",type(something))
	answer = 24 + something
	
	print("the answer is", answer)

def activity6():
	x1 = eval(input("Enter the first number : "))
	x2 = eval(input("Enter the second number : "))
	s = x1 + x2
	d = x1 - x2
	p = x1 * x2
	q = x1 / x2
	
	solution = ((x1 / x2) * 100 - 5 ) // 300
	print("\nThe sum of", x1,"and",x2, "is" , s)
	print("The difference of",x1 ,"and", x2, "is", d)
	print("The product of",x1,"and", x2, "is", p)
	print("The quotient of",x1,"and",x2,  "is", q)
	print("The quotient of", x1, "and",x2,  "is", x1**x2)
	print("The remainder of", x2, "and", x2, "is", x1 % x2)
	print("The floor division of", x1, "and", x2, "is", x1//x2)

def activity7():
	a = 13
	
	print("The value of a is ", a)
	
	a +=3
	a -=4
	a *=5
	a /=6 
	
	print("The vaue of a is ", a)
	
def activity8():
	balance = 5000
	withdrawal  = 2500
	print(balance != withdrawal)
	
	a = 24
	b = 13
	
	print(a > b)

def activity9():
	username = 'yannie'
	password = 'broccoli' 
	
	print(username == 'yannie')
	print((username == 'yannie') and (password != 'broccoli'))
	print((username == 'yannie') or (password == 'broccoli'))
	
def activity10():
	name = input("Input your name ---> ")
	isStudent = input("Are you a student (Yes/No) --> ")
	fare = eval(input("bayad --> "))
	if isStudent == "yes" :
	       discount = fare * .2
	       new_fare = fare - discount
	       print("Hi", name, " student discount is ", discount, " Discounted fare is ", new_fare)
	else:
	       print("Sorry ", name, " you are not eligible for student discount")
        
def activity11():
	#temperature_check
	#1 to 20 cold
	#21 to 30 lukewarm
	#31 to 40 warm
	#41 to 50 hot
	#51 and above boiling hot
	
	temp = eval(input("Enter temperature - - > "))
	 
	if temp >= 1 and temp <= 20:
	 print("Temperature outside is cold")
	elif temp >= 21 and temp <= 30:
	  print("Temperature outside is lukewarm")
	elif temp >= 31 and temp <= 40:
	    	print("Temperature outside is warm")
	elif temp >= 41 and temp <= 50:
	 	print("Temperature outside is hot")
	elif temp >= 51:
	 	print("Temperature outside is boiling hot")
	else:
	 	print("Invalid Temperature")
	 	
def activity12():
	for y in range(1,20,1):
	 print(y,"-Hello World")

def activity13():
	#using loop, ask user to input 15 numbers
	#after input, get the summation of all numbers
	
	numero = 5
	for y in range(1,15):
	 n = eval(input("Enter a number: "))
	 numero += n 
	 print('total number ay', numero)
	 print(numero) 
	 
def activity14():
	#ascending order
	#descending order 10 - 1
	
	for y in range (11, 1, - 1):
		print(y)
		
def activity15():
	odd_sum = 0
	
	for y in range(1,11,1):
	       an = eval(input(f"{y} - Enter a number ---> "))
	       if an %2 == 1:
	              odd_sum += an
	
	print(f"The sum of all the ODD numbers given is {odd_sum}")
	
def activity16():
	for y in range(1, 11, 1):
	       print(y, end="---->")
	       
	       
def activity17():
	for y in range(1, 11, 1):
	    for i in range(1, y, 1):
	              print(i, end="  ")
	print()
	 
def activity18():
	for x in range(1, 11, 1):
	       for y in range(1, x, 1):
	               print(y, end=' ')
	print()
	
def activity19():
	for x in range(1, 11, 1):
	       for y in range(1, x, 1):
	               print(" * ", end=' ')
	print()
	
def activity20():
	for i in range(1, 11, 1):
	       # for j in range(1, i, 1):
	       #             print(" ", end=' ')
	       for z in range(10, i, -1):
	               print(" * ", end= "  ")
	print()
	       
def activity21():
	#washing machine while loop
	isClean = True
	
	while isClean == True:
	       ask = input("Are the clothes clean already (y/n) --> ")
	       if ask.lower() == 'y' :
	               print("Loop continue")
	               continue
	       else:
	               print("Loop Stops")
	               break
	               
def activity22():
	import random
	
	num = random.randint(1,10)
	
	trays = 5
	
	while trays != 0:
	   guess_num = int(input("Guess the number from 1-10: "))
	   trays -= 1
	   
	   if guess_num != num:
	       print("Sorry! Your Guess is Wrong\n")
	   elif guess_num == num:
	       print("Congratulation!")
	       print(f"the number is {num}")
	       print(f"Your remaining tries is {trays}")
	       
	print("\r\rYou are out of Tries")
    
def activity23():
	# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
	# print(months)
	# months.append("Aug")
	# months.append("Sept")
	# months.append("Oct")
	# months.append("Nov")
	# months.append("Dec")
	# print(months)
	# months.pop()
	# print(months)
	# months.append("Dec")
	# print(months)
	
	# #iteration
	# for month in months
	#       print(f"{month}, 2025")
	# for m in months[8 : 12]:
		#           print(f"The bermonths are: {m}")
	# name
	full_name = "Princess Diane B. Salumbides"
	name = list(full_name)
	print(name)
	
	for i in full_name[0 : 4]:
	       print(i)
	name.reverse()
	print(name)
	
def activity24():
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

def activity25():
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
               
	#Creating a Menu Options with While loop and functions
	
	name = input("Hi, What is your name ---> ")
	print(f"Welcome  {name}, to my Compiler Program ")
	
	isContinue = True
	
	while isContinue == True:
	       print("Select a Program")
	       print("A - Activity1\nB - Activity2\nC - Activity15\nD - Multiplication\nF - Factorial\nE - Exit")
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
	               multiplication()
	               continue
	       elif choose == 'f':
	               factorial()
	               continue
	       elif choose == 'e':
	               print("System Exit")
	               break
	       else:
	               print("Invalid Choice")
	              
def activity26():
	color_meaning = ['Pink', 'Blue', 'Green', 'Red', 'Brown', 'Yellow']
	
	#dictionary
	
	color_meaning_1 = {'girly' : 'Pink', 'peace' : 'Blue', 'nature' : 'Green', 'love' : 'Red','comfort' : 'Brown', 'joy' : 'Yellow'}
	
	print(color_meaning_1['girly'])
	
def activity27():
	print("Adding data to dictionary")
	print("=================================")
	tuloy = True
	
	empty_dictionary = {}
	
	def print_anime():
	               for i, j, in empty_dictionary.items():
	               	print(f"CODE {i} TITLE -- {j}")
	def pang_search(key):
	       print("searching . . . ")
	       print(f"result shows {empty_dictionary[key]} on our database")
	
	while tuloy == True:
	       keys = input("Input keys for this anime ---> ")
	       value = input("Enter anime title ---> ")
	       empty_dictionary[keys] = value
	       
	       choice = input("Would you like to continue adding anime \nY - Yes\nN - No\nP - PRINT\nS - Search\n -- > ").lower()
	       
	       if choice == 'y':
	               print("Continuing . . . . . ")
	               continue
	       if choice == 'n':
	               print("Program Stops")
	               break
	       if choice == 'p':
	               print_anime()
	               continue
	       if choice == 's':
	               code = input("Please input the code of the anime --> ")
	               pang_search(code)
	               continue
	       else:
	               print("Invalid Choice, Please try again")
	               continue
                
def activity28():
	#Step 1 
	import pygame
	import time
	import random
	
	# Initialize Pygame
	pygame.init()
	
	# Screen size
	width = 600
	height = 400
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Snake Game')
	
	# Colors (RGB)
	white = (255, 255, 255)
	black = (0, 0, 0)
	red = (213, 50, 80)
	green = (0, 255, 0)
	
	# Game speed and block size
	clock = pygame.time.Clock()
	speed = 10
	snake_block = 10
	
	# Font for messages
	font_style = pygame.font.SysFont(None, 30)
	
	#Step 2 
	def draw_snake(snake_list):
	       	for block in snake_list:
	       		pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])
	
	#Step3
	def game_loop():
	    	game_over = False
	    	game_close = False
	    	
	    	# Starting position of the snake
	    	x = width / 2
	    	y = height / 2
	    	
	    	x_change = 0
	    	y_change = 0
	    	
	    	snake_list = []
	    	length_of_snake = 1
	    	
	    	# Generate first food
	    	food_x = round(random.randrange(0, width - snake_block) / 10) * 10
	    	food_y = round(random.randrange(0, height - snake_block) / 10) * 10
	    	while not game_over:
	    	      #loss screen
	    	      while game_close:
	    	      	screen.fill(black)
	    	      	message = font_style.render('You Lost! Press Q-Quit or C-Play Again', True, red)
	    	      
	    	      screen.blit(message, [width / 6, height / 3])
	    	      pygame.display.update()
	    	      
	    	      for event in pygame.event.get():
	    	              	if event.type == pygame.KEYDOWN:
	    	              	   if event.key == pygame.K_q:
	    	              	   	game_over = True
	    	              	   	game_close = False
	    	              	   
	    	              	   elif event.key == pygame.K_c:
	    	              	   	game_loop()
	    	# Event handling (keyboard)
	    	for event in pygame.event.get():
	    	      		if event.type == pygame.QUIT:
	    	      			game_over = True
	    	      		
	    	      		if event.type == pygame.KEYDOWN:
	    	      		      if event.key == pygame.K_LEFT:
	    	      		      	x_change = -snake_block
	    	      		      	y_change = 0
	    	      		      
	    	      		      elif event.key == pygame.K_RIGHT:
	    	      		      	x_change = snake_block
	    	      		      	y_change = 0
	    	      		      
	    	      		      elif event.key == pygame.K_UP:
	    	      		      	y_change = -snake_block
	    	      		      	x_change = 0
	    	      		      
	    	      		      elif event.key == pygame.K_DOWN:
	    	      		      	y_change = snake_block
	    	      		      	x_change = 0
	    	# Check if snake hits the wall
	    	if x >= width or x < 0 or y >= height or y < 0:
	    		game_close = True
	    		
	    	# Update position
	    	x += x_change
	    	y += y_change
	    	
	    	# Draw background and food
	    	screen.fill(black)
	    	pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
	    	
	    	# Add snake head
	    	snake_head = [x, y]
	    	snake_list.append(snake_head)
	    	
	    	# Remove extra segments if not growing
	    	if len(snake_list) > length_of_snake:
	    		del snake_list[0]
	    	
	    	# Check self-collision
	    	for segment in snake_list[:-1]:
	    	          if segment == snake_head:
	    	          	game_close = True
	    	
	    	# Draw the snake
	    	draw_snake(snake_list)
	    	
	    	# Update display
	    	pygame.display.update()
	    	
	    	# Check if snake eats food
	    	if x == food_x and y == food_y:
	    	      food_x = round(random.randrange(0, width - snake_block) / 10) * 10
	    	      food_y = round(random.randrange(0, height - snake_block) / 10) * 10
	    	      length_of_snake += 1
	    	      
	    	# Control game speed
	    	clock.tick(speed)
	    	
	    	# Quit Pygame
	    	pygame.quit()
	    	quit()
	    	
	    	# Start the game
	    	game_loop()
