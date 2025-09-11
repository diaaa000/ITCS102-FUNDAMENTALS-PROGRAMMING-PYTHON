print("Haro! Welcome to MangaRecoos")
print("Please choose the manga you want to find your next read:P")

genre = input("\nWhat genre do you like? (Adventure, Horror, Romance): ")

#Adventure
if genre == "Adventure":
    length = input("\nHow long do you want your Adventure Manga be? (Short, Long): ")
    if length == "Short":
        decade = input("\nWhich decade do you want your Adventure Manga? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nHere are the Long Adventure Mangas in the year 2000s:\n\tNaruto by Masashi Kishimoto\n\tHunter X Hunter by Yoshihiro Togashi")
        elif decade == "2010s":
            print("\nHere are the Long Adventure Mangas in the year 2010s:\n\tOne piece by Eiichiro Oda\n\tDragon ball by Akira Toriyama")
    elif length == "Long":
        decade = input("\nWhich decade? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nHere are the Short Adventure Mangas in the year 2000s:\n\tInuyasha by Rumiko Takahashi\n\tThe Cat Returns by Reiko Yoshida")
        elif decade == "2010s":
            print("\nHere are the Short Adventure Mangas in the year 2010s:\n\tNoragami by Adachitoka\n\tTower of God by Lee Jong-hui")

#Horror
elif genre == "Horror":
    length = input("\nHow long do you want your Horror Manga be? (Short, Long): ")
    if length == "Short":
        decade = input("\nWhich decade do you want your Horror Manga be? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nHere are the Long Horror Mangas in the year 2000s:\n\tDeath Note by Tsugumi Ohba\n\tUzumaki by Junji Ito")
        elif decade == "2010s":
            print("\nHere are the Long Horror Mangas in the year 2010s:\n\tShiver by Junji Ito\n\tTokyo Ghoul by Sui Ishida")
    elif length == "Long":
        decade = input("\nWhich decade do you want your Horror Manga be? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nHere are the Short Horror Mangas in the year 2000s:\n\tTomie by Junji Ito\n\tMonster by Naoki Urasawa")
        elif decade == "2010s":
            print("\nHere are the Short Horror Mangas in the year 2010s:\n\tAnother by Yukito Ayatsuji\n\tPumpkin Night by Masaya Hokazono")
   
#Romance
elif genre == "Romance":
    length = input("\nHow long should the manga be? (Short, Long): ")
    if duration == "short":
        decade = input("\nWhich decade? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nI can recommend:\n\tThe Enigma of Amigara Fault by Junji Ito")
        elif decade == "2010s":
            print("\nI can recommend:\n\tFragments of Horror by Junji Ito")
    elif duration == "medium":
        decade = input("\nWhich decade? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nI can recommend:\n\tThe Drifting Classroom by Kazuo Umezu")
        elif decade == "2010s":
            print("\nI can recommend:\n\tI Am a Hero by Kengo Hanazawa")
    elif duration == "long":
        decade = input("\nWhich decade? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nI can recommend:\n\tHellsing by Kouta Hirano")
        elif decade == "2010s":
            print("\nI can recommend:\n\tAjin: Demi-Human by Gamon Sakurai")

else:
    print("\n\tSorry but that genre isn't available. Please try again.")
