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
