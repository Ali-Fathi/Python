# TODO: 1 program greeting 
print("Welcome to Tip Calculator!")
# TODO: 2 Ask for total bill
bill = float(input("What is your total bill?\n$"))
# TODO: 3 Ask for tip amount in percent
tip_amount = int(input("What percent tip would like to give? 10, 12 or 15 \n"))
# TODO: Number of people sharing the bill
num_of_people = int(input("How many people are sharing the bill?\n"))

# Calculation 
tip_as_percent = tip_amount / 100
bill_with_tip = (bill * tip_as_percent) + bill 
bill_for_each_person = round(bill_with_tip / num_of_people, 2)
print(f"Each person would pay: ${bill_for_each_person}")
