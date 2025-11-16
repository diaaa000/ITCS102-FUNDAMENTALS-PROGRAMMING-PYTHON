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
	
	
