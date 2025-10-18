loan_amount = eval(input("Enter loan amount: $"))
loan_period = eval(input("Enter loan period in years: "))

loan_period *= 12
principal = loan_amount / loan_period
balance = loan_amount
interest = 0

print("PAYMENT SCHEDULE")
print("------------------------------------------------------------------------------")
print("Month\t|   Monthly Payment\t|   Interest\t|   Principal\t|   Remaining loan\t|")
print("------------------------------------------------------------------------------")
for i in range(1, loan_period + 1, 1):
	balance -= principal
	interest = balance * 0.03
	monthly = interest = principal
	print(f"{i}\t|          {round(monthly, 2)}     \t|     {round(interest, 2)}     \t|     {round(principal, 2)}          \t|")
	 
