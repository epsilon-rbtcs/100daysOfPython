# Day 2 of 100 Days of Python - Tip Calculator

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate total bill including tip
total_bill = bill + (bill * tip / 100)

# Calculate amount per person, rounded to 2 decimal places
amount = round(total_bill / people, 2)

print(f"Each person should pay: ${amount}")