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
	
