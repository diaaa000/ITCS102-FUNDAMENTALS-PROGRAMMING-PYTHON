x1 = eval(input("Enter the first number : "))
x2 = eval(input("Enter the second number : "))
s = x1 + x2
d = x1 - x2
p = x1 * x2
q = x1 / x2

solution = ((x1 / x2) * 100 - 5 ) // 300
print("The sum of", x1,"and",x2, "is" , s)
print("The difference of",x1 ,"and", x2, "is", d)
print("The product of",x1,"and", x2, "is", p)
print("The quotient of",x1,"and",x2,  "is", q)
print("The quotient of", x1, "and",x2,  "is", x1**x2)
print("The remainder of", x2, "and", x2, "is", x1 % x2)
print("The floor division of", x1, "and", x2, "is", x1//x2)