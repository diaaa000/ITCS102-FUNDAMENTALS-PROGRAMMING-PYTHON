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
