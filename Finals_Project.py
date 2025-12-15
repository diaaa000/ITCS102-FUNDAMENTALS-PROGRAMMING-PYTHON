# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Finals Project for ITCS102
# An Interactive Menu Program in Python
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def pause():
    input("\nPress S to to Start ---> ")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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
        #	     print(" ", end=' ')
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
	def multiplication():
		an = int(input("Enter a number: --> "))
		print(f"Multiplication Table for {an}: ")
		for y in range(1,11):
			result = an * y
			print(f"{an} × {y} = {result}")
	def factorial():
		an = eval(input("Enter a number : --> "))
		result = 1
		for y in range (an, 0, -1):
			print(result, "*", y, " = ", result)
			result *= y 
		print("Factorial is", result)
	name = input("Hi, What is your name ---> ")
	print(f"Welcome  {name}, to my Compiler Program ")
	isContinue = True
	while isContinue == True:
		print("Select a Program")
		print("A - Activity1\nB - Activity2\nC - add_odd\nD - Multiplication\nF - Factorial\nE - Exit")
		choose = input("What program / code would you like to run ---> ").lower()
		if choose == 'a':
			activity1()
			continue
		elif choose == 'b':
			activity2
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
		else :
			print("I'm sorry, the option you've chosen is not available now, Please try again later.")
               
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
	import pygame
	import time
	import random
	pygame.init()
	width = 600
	height = 400
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Snake Game')
	white = (255, 255, 255)
	black = (0, 0, 0)
	red = (213, 50, 80)
	green = (0, 255, 0)
	clock = pygame.time.Clock()
	speed = 10
	snake_block = 10
	font_style = pygame.font.SysFont(None, 30)
	def draw_snake(snake_list):
		for block in snake_list:
			pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])
	def game_loop():
		game_over = False
		game_close = False
		x = width / 2
		y = height / 2
		x_change = 0
		y_change = 0
		snake_list = []
		length_of_snake = 1
		food_x = round(random.randrange(0, width - snake_block) / 10) * 10
		food_y = round(random.randrange(0, height - snake_block) / 10) * 10
		while not game_over:
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
		if x >= width or x < 0 or y >= height or y < 0:
			game_close = True
		x += x_change
		y += y_change
		screen.fill(black)
		pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
		snake_head = [x, y]
		snake_list.append(snake_head)
		if len(snake_list) > length_of_snake:
			del snake_list[0]
		for segment in snake_list[:-1]:
			if segment == snake_head:
				game_close = True
		draw_snake(snake_list)
		pygame.display.update()
		if x == food_x and y == food_y:
			food_x = round(random.randrange(0, width - snake_block) / 10) * 10
			food_y = round(random.randrange(0, height - snake_block) / 10) * 10
			length_of_snake += 1
		clock.tick(speed)
		pygame.quit()
		quit()
	game_loop()

def code_challenge1():
    name  = input()
    print("\t\t\t\t* \n\n\t\t\t*\n\n\t\t*\t\t\t*\n\t*\n\n\t\t\t\t Hello Peeps\t\t*\n\n*\t\t\t\t", "\t\t\t\t*\n\n\t*\t\t\t\t\t\t*\n\n\t\t*\n\n\t\t\t\t\t\t*\n\n \t\t\t\t\t*\n\t\t\t*\n\n\t\t\t\t*")
	
def code_challenge2():
    name = input("What is your name? ")
    print("Hi", name , "Welcome to YS Bank")
    
    amount = int(input("Enter amount to deposit: "))
    y1 = amount // 1000
    amount = amount % 1000
    y2 = amount // 500
    amount = amount % 500
    y3 = amount // 200
    amount = amount % 200
    y4 = amount // 100
    amount = amount % 100
    y5 = amount // 50 
    amount = amount % 50
    y6 = amount // 20
    amount = amount % 20
    y7 = amount // 10
    amount = amount % 10
    y8 = amount // 5
    amount = amount % 5
    y9 = amount // 1
    amount = amount % 1
    
    print("Php1000:",y1)
    print("Php500:",y2)
    print("Php200:",y3)
    print("Php100:",y4)
    print("Php50:",y5)
    print("Php20:",y6)
    print("Php10:",y7)
    print("Php5:",y8)
    print("Php1:",y9)
    
    text = input("\nThank you for banking with us!")

def code_challenge3():
	#code_challenge3
	#username_and_password
	
	username = input('Input username: ')
	password = input('Enter password: ')
	
	uname = "dia"
	p_input = "broocs"
	
	if username == uname and password == p_input:
		print("Access granted")
	else:
		print("Access denied")
          
def code_challenge4():
	#code_challenge4
	#is_it_odd_or_even
	
	number = eval(input("Enter a number: "))
	
	if number % 2 == 0:
		print("The number is even.")
	else:
		print("The number is odd.")

def code_challenge5():
	print("Haro! Welcome to MangaRecoos")
	print("Please choose the manga you want to find your next read:P")
	
	genre = input("\nWhat genre do you like? (Adventure, Horror, Romance): ")
	
	#Adventure
	if genre == "Adventure":
		length = input("\nHow long do you want your Adventure Manga be? (Short, Long): ")
	if length == "Short":
		decade = input("\nWhich decade do you want your Adventure Manga? (2000s, 2010s): ")
	if decade == "2000s":
		print("\nHere are the Short Adventure Manga's in the year 2000s:\n\tNaruto by Masashi Kishimoto\n\tHunter X Hunter by Yoshihiro Togashi")
	elif decade == "2010s":
		print("\nHere are the Short Adventure Manga's in the year 2010s:\n\tOne piece by Eiichiro Oda\n\tDragon ball by Akira Toriyama")
	elif length == "Long":
		decade = input("\nWhich decade do you want your Adventure Manga? (2000s, 2010s): ")
	if decade == "2000s":
		print("\nHere are the Long Adventure Manga's in the year 2000s:\n\tInuyasha by Rumiko Takahashi\n\tThe Cat Returns by Reiko Yoshida")
	elif decade == "2010s":
		print("\nHere are the Long Adventure Manga's in the year 2010s:\n\tNoragami by Adachitoka\n\tTower of God by Lee Jong-hui")
	           
	 #Horror
	elif genre == "Horror":
		length = input("\nHow long do you want your Horror Manga be? (Short, Long): ")
	if length == "Short":
		decade = input("\nWhich decade do you want your Horror Manga be? (2000s, 2010s): ")
	if decade == "2000":
		print("\nHere are the Short Horror Manga's in the year 2000s:\n\tDeath Note by Tsugumi Ohba\n\tUzumaki by Junji Ito")
	elif decade == "2010s":
		print("\nHere are the Short Horror Manga's in the year 2010s:\n\tShiver by Junji Ito\n\tTokyo Ghoul by Sui Ishida")
	elif length == "Long":
		decade = input("\nWhich decade do you want your Horror Manga be? (2000s, 2010s): ")
	if decade == "2000s":
		print("\nHere are the Long Horror Manga's in the year 2000s:\n\tTomie by Junji Ito\n\tMonster by Naoki Urasawa")
	elif decade == "2010s":
		print("\nHere are the Long Horror Manga's in the year 2010s:\n\tAnother by Yukito Ayatsuji\n\tPumpkin Night by Masaya Hokazono")
	
	#Romance
	elif genre == "Romance":
		length = input("\nHow long do you want your Romance manga be? (Short, Long): ")
	if length == "Short":
		decade = input("\nWhich decade do you want your Romance Manga be? (2000s, 2010s): ")
	if decade == "2000s":
		print("\nHere are the Short Romance Manga's in the year 2000s:\n\tFruits Basket by Natsuki Takaya\n\tKaichou wa Maid Sama by Hiro Fujiwara")
	elif decade == "2010s":
		print("\nHere are the Short Romance Manga's in the year 2010s:\n\tHorimiya by Daisuke Hagiwara\n\tAo Haru Ride by Io Sakisaka")
	if length == "Long":
		decade = input("\nWhich decade do you want your Romance Manga be? (2000s, 2010s): ")
	if decade == "2000s":
		print("\nHere are the Long Romance Manga's in the year 2000s:\n\tKamisama Hajimemashita by Julietta Suzuki\n\tOuran High School Host Club by Bisco Hatori ")
	elif decade == "2010s":
		print("\nHere are the Long Romance Manga's in the year 2010s:\n\tHoney Lemon Soda by Murata Mayu\n\tSnow White with The Red Hair by Sorata Akituki")
	else:
		print("\n\tSorry but the genre you want is not available right now, Please choose another one")
          
def code_challenge6():
	#FACTORIAL PROGRAM
	an = eval(input("Enter a number : --> "))
	
	result = 1
	for y in range (an, 0, -1):
		print(result, "*", y, " = ", result)
		result *= y 
	print("Factorial is", result)
     
def code_challenge7():
	#summation of odd numbers
	#loop 10 times
	sum_of_odd = 0
	for y in range(10):
		n = int(input(f"Enter a number: "))
		if n % 2 != 0:
			sum_of_odd += n
	print("The sum of all the odd numbers is", sum_of_odd)

def code_challenge8():
	#MULTIPLICATION TABLE
	an = int(input("Enter a number: --> "))
	print(f"Multiplication Table for {an}: ")
	for y in range(1,11):
		result = an * y
		print(an,"x", "y", "=", result)

def code_challenge9():
	#COUNTDOWN TIMER SIMULATOR
	import time
	
	start = int(input("Enter starting number: ---> "))
	
	print("Countdown Started:")
	time.sleep(1)
	
	for y in range(start, -1, -1):
		print(y)
		time.sleep(1)
	print("\nLiftoff!")

def code_challenge10():
	for i in range(1, 11, 1):
		for j in range(10, i, -1):
			print(" ", end= '  ')
		for x in range(1, i, 1):
			print(" * ", end= " ")
		for z in range(1, i, 1):
			print(" * ", end= " ")
		print()
		
	print("\t\t *", end=" ")
	for i in range(1, 11, 1):
		for j in range(10, i, -1):
			print(" ", end= '  ')
		for x in range(1, i, 1):
			print(" * ", end= " ")
		for z in range(1, i, 1):
			print(" * ", end= " ")
		print()
            
def code_challenge11():
	for i in range(1, 11, 1):
		for j in range(10, i, -1):
			print(" ", end= '  ')
		for x in range(1, i, 1):
			print(" * ", end= " ")
		for z in range(1, i, 1):
			print(" * ", end= " ")
		print()
	for i in range(1, 11, 1):
		for j in range(1, i, 1):
			print(" ", end= "  ")
		for x in range(10, i, -1):
			print(" * ", end= " ")
		for z in range(10, i, -1):
			print(" * ", end= " ")
		print()

def code_challenge12():
	for i in range(1, 7, 1):
		for x in range(7, i, -1):
			print('  ', end= " ")
		for y in range(i, 0, -1):
			print(y, end= " ")
		for z in range(2, i + 1, 1):
			print(z, end= " ")
		print()

def code_challenge13():
	#xmasturiii
	for a in range(2, 6, 1):
		for b in range(0, 7):
			print(" ", end=" ")
		for c in range(6, a, -1):
			print(" ", end=" ")
		for d in range(3, a):
			print("¬", end=" ")
		for e in range(2, a, 1):
			print("¬", end=" ")
		print()
	for a2 in range(1, 3, 1):
		for b2 in range(0, 7):
			print(" ", end=" ")
		for c2 in range(0 - 1, a2, 1):
			print(" ", end=" ")
		for d2 in range(2, a2, -1):
			print("¬", end=" ")
		for e2 in range(3, a2, -1):
			print("¬", end=" ")
		print()
	for a3 in range(2, 9, 1):
		for b3 in range(12, a3, -1):
			print(" ", end=" ")
		for c3 in range(2, a3, 1):
			print("¬", end=" ")
		for d3 in range(1, a3):
			print("¬", end=" ")
		print()
	for a4 in range(2, 10, 1):
		for b4 in range(12, a4, -1):
			print(" ", end=" ")
		for c4 in range(1, a4):
			print("¬", end=" ")
		for d4 in range(2, a4):
			print("¬", end=" ")
		print()
	for a5 in range(2, 13, 1):
		for b5 in range(12, a5, -1):
			print(" ", end=" ")
		for c5 in range(1, a5):
			print("¬", end=" ")
		for d5 in range(2, a5):
			print("¬", end=" ")
		print()
	for a6 in range(1,7):
		for b6 in range(1,9):
			print(" ", end=" ")
		for c6 in range(1,9):
			print("", end="¬")
		print()

def code_challenge14():
	print("Hi ! What is your name ---> ")
	print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print("ODD number compiler, type '0' to terminate the loop")
	
	sum = 0
	odd = " "
	tuloy = True
	
	while tuloy == True:
		num = eval(input("Please input a number --> "))
		if num % 2 == 1:
			print("ODD number detected")
			odd += str(num) + " , "
			sum += num
			continue
		elif num == 0:
			print("Loop Terminated")
			break
		else:
			if num % 2 == 0:
				print("EVEN number, skipping . . . ")
			else:
				print("Invalid Number")
				continue
	                       	
	print(f"Haro, The sum of all ODD number is {sum}")
	print(f"All the ODD numbers you input is {odd}")
	
def code_challenge15():
	#List of Animes 
	#Using of list and while loop
	#Animeeeeeee
	print("List of Anime Titles")
	
	anime = [] #empty list
	z = True   
	
	while z == True:
		y = input("Put a Title of an Anime: ")
		print("Anime Added to your Anime List")
		anime.append(y) #all of the title you input will go to your  list
		if y == "exit": #stopper
			print("It's all done, now, you are exiting!!")
			anime.pop() #will remove the string exit to list
			break    #stopper of the loop
	
	print(f"Here are all of the Title of your Anime: ") 
	for x in anime:     #will print all of the anime you inputted, from up to down
		print(f"- {x}")
		
def code_challenge16():
	import os
	import time
	import json
	
	# os.sytstem('cls)
	print("Student Information System")
	print("---------------------------")
	
	student_list = {}
	
	def review_fav_list():
		for i,s in student_list.items():
			print(f"Student Id: {i}, Student Name: {s}")
		print("This will ends in....")
	def delete():
		print(f"Student Id number {student_list[code]} is remove to the list")
		countdown()
	os.system('cls')
	# code = input("Enter Student ID to delete: ")
	# if code in student_list:
	#   removed_student = student_list.pop(code)  # Safely remove by key
	#   print(f"Student ID {code} ({removed_student[0]} {removed_student[1]}{removed_student[2]}) has been removed from the list.")
	#   countdown()
	#   os.system('cls')
	def countdown():
		for i in range(1,4):
			print(i)
			time.sleep(1)
	while True:
		os.system("cls")
		print("Select the option below:\n A - Add information\n B - Search a Record\n C - Delete a Record\n D - Review a Record\n E - Modify the List\n F - Export Student Record\n G - Import Student Record\n H - Exit the program")
		option = input("Enter your option: ").lower()
		if option == "a":
			Search_cod = input("Student Id: ")
			first_name = input("Enter First name: ").capitalize()
			last_name = input("Enter Last name: ").capitalize()
			course = input("Student Course: ").upper()
			# student_list = {Search_cod : [first_name, last_name, course]}
			student_list[Search_cod] = [first_name, last_name, course]
			print("DATA SAVED")
			countdown()
			os.system('cls')
		
		elif option == "b":
			code = input("Enter Student Id: ")
			print(f"Result shows is {student_list[code]}")
			print("Record Found")
			countdown()
			os.system('cls')
			continue
		
		elif option == "c":
			code = input("Enter Student Id: ")
			if code in student_list:
				del student_list[code]
				print(f"Student Id number {student_list[code]} is remove to the list")
				countdown()
				os.system('cls')
			else:
				print("The Student Id is not found")
		
		elif option == "d":
			review_fav_list()
			countdown()
			os.system('cls')
		
		elif option == "e":
			while True:
				code = input("Enter the code you want to change: ")
				print(f"Result shows is {student_list[code]}")
				edit = int(input("Option to edit\n Type the number\n 1. First name\n 2. Last name\n 3. Course\n----> "))
				if edit == 1:
					print("Editing First Name")
					new = input("Enter a new First Name: ").capitalize()
					student_list[code][0] = new # para mabago yung values
				elif edit == 2:
					print("Editing Last Name")
					new = input("Enter a new Last Name: ").capitalize()
					student_list[code][1] = new
				elif edit == 3:
					print("Editing Course")
					new = input("Enter a new Course: ").upper()
					student_list[code][2] = new
				else:
					print("Invalid choose")
					print(f"{student_list[code]} Is the new Student Data")
					option = input("Do you want to edit again?(yes/no) ").lower()
					if option == "yes":
						continue
					elif option == "no":
						os.system("cls")
						break
				# isa = input("Do you want to edit another data")
				# if option == "yes":
				#   continue
				# elif option == "no":
				#   os.system("cls")
				#   break

		elif option == "f":
			os.system("cls")
			print("Export Student Record")
			# file name, read(r) for Import/ write(w) for Export
			with open('student_record.json','w') as new_file:
				json.dump(student_list, new_file, indent=4)
				print("DATA EXPORTED TO JSON")
				countdown()
				os.system('cls')

		elif option == "g":
			os.system("cls")
			print("Import Student Record")
	   	 	# file name, read(r) for Import/ write(w) for Export
			with open('student_record.json','r') as new_file:
				student_json = json.load(new_file)
			student_list = student_json
			print("DATA IMPORTED TO JSON")
			countdown()
			os.system('cls')
		
		elif option == "h":
			os.system("cls")
			print("Exiting The Program........")
			countdown()
			os.system("cls")
			exit()
		
		else:
			print("Invalid")
			os.system('cls')
			
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Selector for the Challenges
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def code_challenge(n):
    if n == 1: code_challenge1()
    elif n == 2: code_challenge2()
    elif n == 3: code_challenge3()
    elif n == 4: code_challenge4()
    elif n == 5: code_challenge5()
    elif n == 6: code_challenge6()
    elif n == 7: code_challenge7()
    elif n == 8: code_challenge8()
    elif n == 9: code_challenge9()
    elif n == 10: code_challenge10()
    elif n == 11: code_challenge11()
    elif n == 12: code_challenge12()
    elif n == 13: code_challenge13()
    elif n == 14: code_challenge14()
    elif n == 15: code_challenge15()
    elif n == 16: code_challenge16()
    else:
        print("Your choice of challenge is not available now, Please try again later.")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# Activity Selector
# >>>>>>>>>>>>>>>>>>>>>>>>>>>

def selected_activity(n):
    if n == 1:
        activity1()
    elif n == 2:
        activity2()
    elif n == 3:
        activity3()
    elif n == 4:
        activity4()
    elif n == 5:
        activity5()
    elif n == 6:
        activity6()
    elif n == 7:
        activity7()
    elif n == 8:
        activity8()
    elif n == 9:
        activity9()
    elif n == 10:
        activity10()
    elif n == 11:
        activity11()
    elif n == 12:
        activity12()
    elif n == 13:
        activity13()
    elif n == 14:
        activity14()
    elif n == 15:
        activity15()
    elif n == 16:
        activity16()
    elif n == 17:
        activity17()
    elif n == 18:
        activity18()
    elif n == 19:
        activity19()
    elif n == 20:
        activity20()
    elif n == 21:
        activity21()
    elif n == 22:
        activity22()
    elif n == 23:
        activity23()
    elif n == 24:
        activity24()
    elif n == 25:
        activity25()
    elif n == 26:
        activity26()
    elif n == 27:
        activity27()
    elif n == 28:
        activity28()
    else:
        print(f"\n--- Activity {n} ---")
        print("The activity s not available now, Please try again later.")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# B - MENU
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def activity_menu():
    while True:
        print("\n----- A_MENU -----")
        for j in range(1, 29):
            print(f"{j}) Activity {j}")
        print("29) Return to A Menu")

        choice = input("Choose your activity: ")

        if not choice.isdigit():
            print("Invalid choice. Please, try again.")
            continue

        choice = int(choice)

        if 1 <= choice <= 28:
            selected_activity(choice)
            pause()
        elif choice == 29:
            break
        else:
            print("Invalid choice. Please, try again.")

def c_challenge_menu():
    while True:
        print("\----- C_MENU -----")
        for j in range(1,17):
            print(f"{j}) Code Challenge {j}")
        print("17) Return to A Menu")

        cc=input("Choose your Challenge: ")
        if cc.isdigit():
            cc=int(cc)
            if 1<=cc<=16:
                code_challenge(cc)
                pause()
            elif cc==17:
                break

# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# A MENU
# >>>>>>>>>>>>>>>>>>>>>>>>>>>

def A_menu():
    while True:
        print("\n------------ A_MENU ------------")
        print("1) Activities 1 - 28")
        print("2) Code Challenges 1 - 16")
        print("3) System Exit")

        choice = input("Your choice: ")

        if choice == "1":
            activity_menu()
        elif choice == "2":
            c_challenge_menu()
        elif choice == "3":
            print("Bye Bye!")
            break
        else:
            print("Invalid Choice.")

# >>>>>>>>>>>>>>>>>>>>>>>>>>
# Program Started
# >>>>>>>>>>>>>>>>>>>>>>>>>>
A_menu()
