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