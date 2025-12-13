#Finals Project
#Python Interactive Menu Program
#Must include all the activities and code challenges
#Must use all of the functions of Python

from Activities import *
from code_challenges import *
import os
import time

def clear():
	os.system('cls')
	
def divider():
	print("\n\n", ",", "·" * 100)
	
def pause():
	time.sleep(0.5)
	
clear()
divider()
first = ("\nWelcome to the WorldPyProgram, Traveler!\nIn this World you'll find the history and beauty of Python")
for text in first:
	print(text, end=' ', flush=True)
	time.sleep(0.01)
divider()

name = input("What do you want to be called, Traveler? ····> ")

clear()
divider()
print(f"\n\nWelcome Traveler {name}, this is the World where you can explore the beauty of Python")
divider()

a = True
while a == True:
	clear()
	divider()
	dash1 = ("\n\nWhere do you want to wonder, Traveler?\n\tI - Thrilling Activities\n\tII - Beauty of Challenges\n\tIII - Guided Menu\nIV - Exit")
	for text in dash1:
		print(text, end=' ', flush = True)
		time.sleep(0.01)
	divider()
	tort = input(f"\nWhere do you want to go first, traveler {name}?···> ").upper()
	
	#Thrilling Activities Choices
	if tort == 'I':
	   print("Greetings, Traveler! Welcome to the Thrilling Activities, Please select the mission you want ···> ")
	divider()
	  print("\nMis1 - Activity1\nMis2 - Activity2\nMis3 - Activity3\nMis4 - Activity4\nMis5 - Activity5\nMis6 - Activity6\nMis7 - Activity7\nMis8 - Activity8\nMis9 - Activity9\nMis10 - Activity10\nMis11 - Activity11\Miss12\n - Activity12\nMis13 - Activity13\nMis14 - Activity14\nMis15 - Activity16\n'Mis17 - Activity17\nMis18 - Activity18\nMis19 - Activity19\nMis20 - Activity20\nMis21 - Activity21\nMis22 - Activity22\nMis23 - Activity23\nMis24 - Activity24\nMis25 - Activity25\nMis26 - Activity26\nMis27 - Activity27\nMis28 - Activity28\nE - Exit")
	divider()
	  
	    if choo = input("What mission would you like to accomplish?···> ").lower()
	   
	   if choo == 'Mis1':
	   	activity1()
	   	continue
	   	
	   elif choo == 'Mis2':
	   	activity2()
	   	continue
	   	
	   elif choo == 'Mis3':
	   	activity3()
	   	continue
	   	
	   elif choo == 'Mis4':
	   	activity4()
	   	continue
	   	
	   elif choo == 'Mis5':
	   	activity5()
	   	continue
	   	
	   elif choo == 'Mis6':
	   	activity6()
	   	continue
	   	
	   elif choo == 'Mis7':
	   	activity7()
	   	continue
	   	
	   elif choo == 'Mis8':
	   	activity8()
	   	continue
	   	
	   elif choo == 'Mis9':
	   	activity9()
	   	continue
	   	
	   elif choo == 'Mis10':
	   	activity10()
	   	continue
	   	
	   elif choo == 'Mis11':
	   	activity11()
	   	continue
	   	
	   elif choo == 'Mis12':
	   	activity12()
	   	continue
	   	
	   elif choo == 'Mis13':
	   	activity13()
	   	continue
	   	
	   elif choo == 'Mis14':
	   	activity14()
	   	continue
	   	
	   elif choo == 'Mis15':
	   	activity15()
	   	continue
	   	
	   elif choo == 'Mis16':
	   	activity16()
	   	continue
	   	
	   elif choo == 'Mis17':
	   	activity17()
	   	continue
	   	
	   elif choo == 'Mis18':
	   	activity18()
	   	continue
	   	
	   elif choo == 'Mis19':
	   	activity19()
	   	continue
	   	
	   elif choo == 'Mis20':
	   	activity20()
	   	continue
	   	
	   elif choo == 'Mis21':
	   	activity21()
	   	continue
	   	
	   elif choo == 'Mis22':
	   	activity22()
	   	continue
	   	
	   elif choo == 'Mis23':
	   	activity23()
	   	continue
	   	
	   elif choo == 'Mis24':
	   	activity24()
	   	continue
	   	
	   elif choo == 'Mis25':
	   	activity25()
	   	continue
	   	
	   elif choo == 'Mis26':
	   	activity26()
	   	continue
	   	
	   elif choo == 'Mis27':
	   	activity27()
	   	continue
	   	
	   elif choo == 'Mis28':
	   	activity28()
	   	continue
	   elif choo == 'E':
	   	print("You have exited the mission")
	   	
	   else:
	   	print("The mission is not available")
	   
	#Beauty of Challenges
	elif tort == 'II':
	   		   print("Greetings, Traveler! Welcome to the Beauty of Challenges, Please select the quest you want ···> ")
	   		   print("\n\tQuestA - Code_Challenge1\n\tQuestB - Code_Challenge2\n\tQuestC - Code_Challenge3\n\tQuestD - Code_Challenge4\n\tQuestQ - Code_Challenge5\n\tQuestF - Code_Challenge6\n\tQuestG - Code_Challenge7\n\tQuestH - Code_Challenge8\n\tQuestI - Code_Challenge9\n\tQuestJ - Code_Challenge10\n\tQuestK - Code_Challenge11\n\tQuestL - Code_Challenge12\n\tQuestM - Code_Challenge13\n\tQuestN - Code_Challenge14\n\tQuestO - Code_Challenge15\n\tQuestP - Code_Challenge16\n\tQuestE - Exit")
	 divider()  		   
	   		   choo = input("What quest would you like to open?···> ").lower()
	   		   
	   		   if choo == 'QuestA':
	   		   	code_challenge1()
	   		   	continue
	   		   elif choo == 'QuestB':
	   		   	code_challenge2()
	   		   	continue
	   		   elif choo == 'QuestC':
	   		   	code_challenge2()
	   		   	continue
	   		   elif choo == 'QuestD':
	   		   	code_challenge3()
	   		   	continue
	   		   elif choo == 'QuestQ':
	   		   	code_challenge4()
	   		   	continue
	   		   elif choo == 'QuestF':
	   		   	code_challenge5()
	   		   	continue
	   		   elif choo == 'QuestG':
	   		   	code_challenge6()
	   		   	continue
	   		   elif choo == 'QuestH':
	   		   	code_challenge7()
	   		   	continue
	   		   elif choo == 'QuestI':
	   		   	code_challenge8()
	   		   	continue
	   		   elif choo == 'QuestJ':
	   		   	code_challenge9()
	   		   	continue
	   		   elif choo == 'QuestK':
	   		   	code_challenge10()
	   		   	continue
	   		   elif choo == 'QuestL':
	   		   	code_challenge11()
	   		   	continue
	   		   elif choo == 'QuestM':
	   		   	code_challenge12()
	   		   	continue
	   		   elif choo == 'QuestN':
	   		   	code_challenge13()
	   		   	continue
	   		   elif choo == 'QuestO':
	   		   	code_challenge14()
	   		   	continue
	   		   elif choo == 'QuestP':
	   		   	code_challenge15()
	   		   	continue
	   		   elif choo == 'QuestE':
	   		   	print("Quest Exit")
	   		   	break
	   		   	
	   		   else:
	   		   	print("The quest is not available now")
	   		   	
 	#Guided Menu of Python
 	elif tort == 'III':
 		clear()
 		while True:
 			divider()
 		dashA = ("\nGreetings, Traveler! Welcome to the Guided Menu, where i'll guide you on the various path of Python\nA - Built in Functions of Python\nB - Python Syntax\nC - Exit")
 		for text in dashA:
 		 print(text, end= ' ', flush=True)
 		 time.sleep(0.01)
 		divider()
 		bum = input("\n\nPick your choice of Guided Menu ···> ").upper()
 		
 		#Built in Functions of Python
 		if bum = 'A':
 			clear()
 			while True:
 				divider()
 				dash1 = ("\n\nYay! You have chosen the guide for Built in Functions\n\n Here are the things that you can learn about Built in Functions\n\nA1 - print()\nA2 - list()\nA3 - len()\nA4 - input()\nA5 - int()\nA6 - dict()")
 				for text in dash1:
 					print(text, end=' ', flush=True)
 					time.sleep(0.01)
 				divider()
 				ow = input("Your choice ···> ").upper()
 				if ow == 'A1':
 					clear()
 					while True:
 						divider()
 						A1 = ("\nYou have chosen the print() function\nWhat would you like to know about print function?\n\nPF1 - Function of Print\nPF2 - Use of Print Function")
 						for text in A1:
 							print(text, end=' ', flush=True)
 							time.sleep(0.01)
 						divider()
 						oi = input("What do you want to known first?: ").upper()
 						
 						if oi == 'PF1':
 							clear()
 							while True:
 								divider()
 								PF1 = ("\nYay! You have chosen the function of print\nPrint\n\t - it prints output to the console.")
 								for text in PF1:
 									print(text, end= ' ', flush=True)
 									time.sleep(0.01)
 								divider()
 						
 						elif oi == 'PF2':
 							clear()
 							while True:
 								divider()
 								PF2 = ("\nYay! You have chosen the use of print function\n\nIt can be use as this:\n\n\tprint("Hello, World!")")
 								
 								for text in PF2:
 									print(text, end= ' ', flush=True)
 									time.sleep(0.01)
 								divider()
 								
 				elif ow == 'A2':
 				  	clear()
 				  	while True:
 				  		divider()
 				  		A2 = ("\nYou have chosen the list() function\nWhat would you like to know about list function?\n\nLF1 - Function of list\nLF2 - Use of list Function")
 				  		for text in A2:
 				  			print(text, end=' ', flush=True)
 				  			time.sleep(0.01)
 				  		divider()
 				  		oc = input("What do you want to know?: ").upper()
 				  		if oc == 'LF1':
 				  			clear()
 				  			while True:
 				  				divider()
 				  				LF1 = ("\nYay! You have chosen the function of list\nList\n\t - it created a list in Python.")
 				  				
 				  				for text in LF1:
 				  					print(text, end= ' ', flush=True)
 				  					time.sleep(0.01)
 				  				divider()
 				  		
 				  		elif oc == 'LF2':
 				  			clear()
 				  			while True:
 				  				divider()
 				  				LF2 = ("\nYay! You have chosen the use of list\n\nit can be use as this:\n\nmylist = ["red", "green", "yellow"]")
 				  				for text in LF2:
 				  					print(text, end= ' ', flush=True)
 				  					time.sleep(0.01)
 				  				divider()
 				 
 				 elif ow == 'A3':
 				 	clear()
 				 	while True:
 				 		divider()
 				 		A3 = ("\nYou have chosen the len() function\nWhat would you like to know about len function?\n\nEF1 - Function of len\nEF2 - Use of len Function")
 				 		for text in A3:
 				 			print(text, end=' ', flush=True)
 				 			time.sleep(0.01)
 				 		divider()
 				 		oc = input("What do you want to know?: ").upper()
 				 		
 				 		if ol == 'EF1':
 				 			clear()
 				 			while True:
 				 				divider()
 				 				EF1 = ("\nYay! You have chosen the function of len\nLen\n\t - it returns the length of the object.")
 				 				
 				 				for text in EF1:
 				 						print(text, end= ' ', flush=True)
 				 						time.sleep(0.01)
 				 						divider()
 							
 						elif ol == 'EF2':
 							clear()
 							while True:
 								divider()
 								EF2 = ("\nYay! You have chosen the use of len\n\nit can be use as this:\n\nmylist = ["red", "green", "yellow"]\nno = len('mylist')\nprint(no)")
 								
 								for text in EF2:
 											print(text, end= ' ', flush=True)
 											time.sleep(0.01)
 								divider()
 				 
 				 elif ow == 'A4':
 				 	clear()
 				 	while True:
 				 		divider()
 				 		A4 = ("\nYou have chosen the input() function\nWhat would you like to know about input function?\n\nIF1 - Function of input\nIF2 - Use of input Function")
 				 		for text in A4:
 				 			print(text, end=' ', flush=True)
 				 			time.sleep(0.01)
 				 		divider()
 				 		oc = input("What do you want to know?: ").upper()
 				 		
 				 		if on == 'IF1':
 				 			clear()
 				 			while True:
 				 		divider()
 				 		IF1 = ("\nYay! You have chosen the function of input\nInput\n\t - take input from the user as a string.")
 				 		
 				 		for text in IF1:
 				 			print(text, end=' ', flush=True)
 				 			time.sleep(0.01)
 				 		divider()
 				 		
 				 		elif on == 'IF2':
 				 			clear()
 				 			while True:
 				 				divider()
 				 				IF2 = ("\nYay! You have chosen the use of input\n\nit can be use as this:\n\nprint("Enter your nickname: ")\na = input()\n\print('Hello, ' + x)")
 				 				for text in IF2:
 				 					print(text, end=' ', flush=True)
 				 					time.sleep(0.01)
 				 				divider()
 				 		
 				  elif ow == 'A5':
 				  	clear()
 				  	while True:
 				  		divider()
 						A5 = ("\nYou have chosen the int() function\nWhat would you like to know about int function?\n\nTF1 - Function of int\nTF2 - Use of int Function")
 						for text in A5:
 							print(text, end=' ', flush=True)
 							time.sleep(0.01)
 							divider()
 							oc = input("What do you want to know?: ").upper()
 							
 							if of == 'TF1':
 								clear()
 								while True:
 									divider()
 									TF1 = ("\nYay! You have chosen the function of int\nInt\n\t - it converts the number in a given base to decimal.")
 									for text in TF1:
 										print(text, end=' ', flush=True)
 										time.sleep(0.01)
 									divider()
 							
 							elif of == 'TF2':
 								clear()
 								while True:
 									divider()
 									TF2 = ("\nYay! You have chosen the use of int\n\nit can be use as this:\n\nno = int(1.5)")
 								
 					elif ow == 'A6':
 							clear()
 							while True:
 								divider()
 								A6 = ("\nYou have chosen the dict() function\nWhat would you like to know about dict function?\n\nDF1 - Function of dict\nDF2 - Use of dict Function")
 								
 								for text in A6:
 									print(text, end=' ', flush=True)
 									time.sleep(0.01)
 								divider()
 								oc = input("What do you want to know?: ").upper()
 								
 								if om == 'DF1':
 									clear()
 									while True:
 										divider()
 										DF1 = ("\nYay! You have chosen the function of dict\nDict\n\t - it creates a Python Data Dictionary.")
 										for text in DF1:
 											print(text, end=' ', flush=True)
 											time.sleep(0.01)
 										divider()
 								
 								elif om == 'DF2':
 									clear()
 									while True:
 										divider()
 										DF2 = ("\nYay! You have chosen the use of dict\n\nit can be use as this:\n\ninfo = dict(name = "Dia", age = 18, country = "Philippines")\nprint(info)")
 										
 										for text in DF1:
 											print(text, end=' ', flush=True)
 											time.sleep(0.01)
 										divider()
 		
 		#Python Modules
 		if bum == 'B':
 			 						clear()
 			 						while True:
 			 							divider()
 			 							dash2 = ("\n\nYay! You have chosen the guide for Python Modules\n\n Here are the things that you can learn about Modules in Python\n\nB1 - Python Indentation\nB2 - Python Variables\nB3 - Comment")
 			 							
 			 							for text in dash2:
 			 								print(text, end=' ', flush=True)
 			 								time.sleep(0.01)
 			 							divider()
 			 							ew = input("Your choice···> ")
 			 							if ew == 'B1':
 			 								clear()
 			 								while True:
 			 									divider()
 			 									B1 = ("\nYou have chosen Python Indentation\n\nPython Indentation\n\nPython Indentation\n\t - Python uses indentation to indicate a block of code.")
 			 									for text in B1:
 			 										print(text, end=' ', flush=True)
 			 										time.sleep(0.01)
 			 									divider()
 			 									
 			 							elif ew == 'B2':
 			 									clear()
 			 									while True:
 			 										divider()
 			 										B2 = ("\nYou have chosen Python Variables\n\nPython Variables\n\t - variables are created when you assign a value to it\n\nExample:\nx = 1")
 			 										
 			 										for text in B2:
 			 											print(text, end=' ', flush=True)
 			 											time.sleep(0.01)
 			 										divider()
 			 							
 			 							elif ew == 'B3':
 			 									clear()
 			 									while True:
 			 										divider()
 			 										B3 = ("\nYou have chosen Comment\n\nComment\n\t - the purpose of commenting in Python is for in-code documentation, it starts with #, that will make Python ignore it.") 
 			 										for text in B3:
 			 											print(text, end=' ', flush=True)
 			 											time.sleep(0.01)
 			 										divider()
