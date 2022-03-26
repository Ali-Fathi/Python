#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Solutin

# TODO: Program greeting
from ctypes.wintypes import FLOAT
from re import T


print("Welcome to the tip calculator!")
# TODO: Ask for total bill
bill = float(input("What's the total bill: $"))
# TODO: Ask for percent for a tip
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# TODO: Ask for people to split the bill
people = int(input("How many people to split the bill? "))

# Calculation
tip_as_percent = float(tip / 100) 
total_bill = float(tip_as_percent * bill) + bill
each_person_bill = round(float(total_bill / people), 2)
print(f"Each person will pay: ${each_person_bill}")