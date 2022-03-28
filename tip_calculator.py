# Tip Calculator

print("Welcome to the tip calculator")
#Collect total of the food bill
bill = float(input("What was the total bill?\n"))





people = int(input("How many people to split the bill?\n"))

amount = total_bill / people

final_amount = "{:.2f}".format(amount)

print(f"Each person should pay {final_amount}")
