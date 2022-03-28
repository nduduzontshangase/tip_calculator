# Tip Calculator

print("Welcome to the tip calculator")
#Collect total of the food bill
bill = float(input("What was the total bill?\n"))

tip = int(input("What percentage tip would you like to give? 10, 12, 15?\n"))

# Tip percent to be given to waiter
tip_amount = (tip / 100) * bill
total_bill = tip_amount + bill
people = int(input("How many people to split the bill?\n"))

amount = total_bill / people
# final_amount = round(amount, 2)
final_amount = "{:.2f}".format(amount)

print(f"Each person should pay {final_amount}")
