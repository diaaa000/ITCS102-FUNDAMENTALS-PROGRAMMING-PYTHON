#code_challenges

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
