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
        if decade == "2000s":
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
    elif length == "Long":
        decade = input("\nWhich decade do you want your Romance Manga be? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nHere are the Long Romance Manga's in the year 2000s:\n\tKamisama Hajimemashita by Julietta Suzuki\n\tOuran High School Host Club by Bisco Hatori ")
        elif decade == "2010s":
            print("\nHere are the Long Romance Manga's in the year 2010s:\n\tHoney Lemon Soda by Murata Mayu"\n\tSnow White with The Red Hair by Sorata Akituki")
else:
    print("\n\tSorry but the genre you want is not available right now, Please choose another one")
