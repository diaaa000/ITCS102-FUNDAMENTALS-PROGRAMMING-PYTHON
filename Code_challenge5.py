print("Haro! Welcome to MangaRecoos")
print("Please choose the manga you want to find your next read:P")

genre = input("What genre of Manga do you want? (Adventure/Horror/Romance): ")

#Adventure
if genre.lower() == "Adventure":
	length = input("How long do you want your Adventure Manga be? (Long/Short): ")
	if length == "Long":
	   decade = input("\n In which decade do you want your Adventure Manga? (2000s/2010s): ")
	   if decade == "2000s":
	       print("\n Here are the Long Adventure Mangas in the year 2000s: \n\t Naruto \n\t Hunter X Hunter \n\t Fairy Tale")
	       if decade == "2010s":
		      print("\n Here are the Long Adventure Mangas in the year 2010s: \n\t One piece \n\t The seven deadly sins \n\t One Punch Man")
			elif length == "Short":
					decade = input("In which decade do you want your Adventure Manga be? (2000s/2010s): ")
					if decade == "2000s":
						print("\n Here are the Short Adventure Mangas in the year 2000s: \n\t Inuyasha \n\t The Cat Returns \n\t Fushigi Yuugi")
						elif decade == "2010s":
							print("\n Here are the Short Adventure Mangas in the year 2010s: \n\t Noragami \n\t Tower of God \n\t Pokemon")
							
							
#Horror
if genre.lower() == "Horror":
	length = input("How long do you want your Horror Manga be? (Long/Short): ")
	if length == "Long":
	    decade = input("\n In which decade do you want your Horror Manga? (2000s/2010s): ")
	    if decade == "2000s":
	    	print("\n Here are the Long Horror Mangas in the year 2000s: \n\t Death Note \n\t Uzumaki \n\t Elfen Lied")
			elif decade == "2010s":
				print("\n Here are the Long Horror Mangas in the year 2010s: \n\t Shiver \n\t Blood C \n\t Tokyo Ghoul")
				elif length == "Short":
					decade = input("In which decade do you want your Horror Manga be? (2000s/2010s): ")
					if decade == "2000s":
						print("\n Here are the Short Horror Mangas in the year 2000s: \n\t The Drifting Classroom \n\t Tomie \n\t Monster")
						elif decade == "2010s":
							print("\n Here are the Short Horror Mangas in the year 2010s: \n\t Another \n\t Pumpkin Night \n\t Chainsaw Man")
							
							
#Romance
if genre.lower() == "Romance":
	length = input("How long do you want your Romance Manga be? (Long/Short): ")
	if length == "Long":
	    decade = input("\n In which decade do you want your Romance Manga? (2000s/2010s): ")
	    if decade == "2000s":
	    	print("\n Here are the Long Romance Mangas in the year 2000s: \n\t Fruits Basket \n\t Kaichou wa Maid Sama \n\t Kimi ni Todoke")
			elif decade == "2010s":
				print("\n Here are the Long Romance Mangas in the year 2010s: \n\t Ao Haru Ride \n\t Horimiya \n\t My Little Monster")
				elif length == "Short":
					decade = input("In which decade do you want your Romance Manga be? (2000s/2010s): ")
					if decade == "2000s":
						print("\n Here are the Short Romance Mangas in the year 2000s: \n\t Kamisama Hajimemashita \n\t Ouran High School Host Club \n\t Cardcaptor Sakura")
						elif decade == "2010s":
							print("\n Here are the Short Romance Mangas in the year 2010s: \n\t Honey Lemon Soda \n\t Orange \n\t Snow White with the Red Hair")

else:
	print("Sorry but the genre you want is not available right now, Please try again.")

							
				

					
			

