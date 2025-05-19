# TODO 1. Create a tip calculator.
# TODO 2. Ask the user for the total bill.
# TODO 3. Ask the user for the tip percentage.
# TODO 4. Ask the user for the number of people to split the bill.
# TODO 5. Calculate the total amount each person should pay.
# TODO 6. Print the result.

print("Welcome to the tip calculator program.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

if tip == 10:
    total_bill = (bill/people) * 1.1
elif tip == 12:
    total_bill = (bill/people) * 1.12
elif tip == 15:
    total_bill = (bill/people) * 1.15

print(f"Each person should pay: ${total_bill:.2f}")



