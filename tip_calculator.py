# Tip Calculator

print("Welcome to the tip calculator")
#Collect total of the food bill
bill = float(input("What was the total bill?\n"))

# Tip percent to be given to waiter
tip = int(input("What percentage tip would you like to give? 10, 12, 15?\n"))

tip_amount = (tip / 100) * bill
total_bill = tip_amount + bill