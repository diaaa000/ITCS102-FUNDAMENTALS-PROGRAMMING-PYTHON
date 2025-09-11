print("Haro! Welcome to MangaRecoos")
print("Please choose the manga you want to find your next read:P")

genre = input("What genre of Manga do you want? (Adventure/Horror/Romance): ")

#Adventure
if genre.lower() == "Adventure":
	length = input("How long do you want your Adventure Manga be? (Long/Short): ")
	if length == "Long":
	   decade = input("In which decade do you want your Adventure Manga? (2000s/2010s): ")
	   if decade == "2000s":
	       print("\nHere are the Long Adventure Mangas in the year 2000s:\n\tNaruto by Masashi Kishimoto\n\tHunter X Hunter by Yoshihiro Togashi")
	       if decade == "2010s":
		      print("\nHere are the Long Adventure Mangas in the year 2010s:\n\tOne piece by Eiichiro Oda\n\tDragon ball by Akira Toriyama")
			elif length == "Short":
					decade = input("\nIn which decade do you want your Adventure Manga be? (2000s/2010s): ")
					if decade == "2000s":
						print("\nHere are the Short Adventure Mangas in the year 2000s:\n\tInuyasha by Rumiko Takahashi\n\tThe Cat Returns by Reiko Yoshida")
						elif decade == "2010s":
							print("\nHere are the Short Adventure Mangas in the year 2010s:\n\tNoragami by Adachitoka\n\tTower of God by Lee Jong-hui")
							
							
#Horror
if genre.lower() == "Horror":
	length = input("How long do you want your Horror Manga be? (Long/Short): ")
	if length == "Long":
	    decade = input("\nIn which decade do you want your Horror Manga? (2000s/2010s): ")
	    if decade == "2000s":
	    	print("\nHere are the Long Horror Mangas in the year 2000s:\n\tDeath Note by Tsugumi Ohba\n\tUzumaki by Junji Ito")
			elif decade == "2010s":
				print("\nHere are the Long Horror Mangas in the year 2010s:\n\tShiver by Junji Ito\n\tTokyo Ghoul by Sui Ishida")
				elif length == "Short":
					decade = input("\nIn which decade do you want your Horror Manga be? (2000s/2010s): ")
					if decade == "2000s":
						print("\nHere are the Short Horror Mangas in the year 2000s:\n\tTomie by Junji Ito\n\tMonster by Naoki Urasawa")
						elif decade == "2010s":
							print("\nHere are the Short Horror Mangas in the year 2010s:\n\tAnother by Yukito Ayatsuji\n\tPumpkin Night by Masaya Hokazono")
							
							
#Romance
if genre.lower() == "Romance":
	length = input("How long do you want your Romance Manga be? (Long/Short): ")
	if length == "Long":
	    decade = input("\nIn which decade do you want your Romance Manga? (2000s/2010s): ")
	    if decade == "2000s":
	    	print("\nHere are the Long Romance Mangas in the year 2000s:\n\tFruits Basket by Natsuki Takaya\n\tKaichou wa Maid Sama by Hiro Fujiwara")
			elif decade == "2010s":
				print("\nHere are the Long Romance Mangas in the year 2010s:\n\tAo Haru Ride by Io Sakisaka\n\tHorimiya by Daisuke Hagiwara")
				elif length == "Short":
					decade = input("\nIn which decade do you want your Romance Manga be? (2000s/2010s): ")
					if decade == "2000s":
						print("\nHere are the Short Romance Mangas in the year 2000s:\n\tKamisama Hajimemashita by Julietta Suzuki\n\tOuran High School Host Club by Bisco Hatori")
						elif decade == "2010s":
							print("\nHere are the Short Romance Mangas in the year 2010s:\n\tHoney Lemon Soda by Murata Mayu\n\tSnow White with the Red Hair by Sorata Akiduki")

else:
	print("Sorry but the genre you want is not available right now, Please try again.")

							
				

					
			
