# TODO 1. Calculation

# function to add 2 numbers
def add(a, b):
    a = float(input("What is first number?\n"))
    b = float(input("What is second number?\n"))
    result = a + b
    print(f"The result of adding {a} and {b} is: {result}") 
# fuction to substract 2 numbers
def sub(a, b):
    a = float(input("What is first number?\n"))
    b = float(input("What is second number?\n"))
    result = a - b
    print(f"The result of substracting {a} and {b} is: {result}")

# function to multiple 2 numbers
def multiply(a, b):
    a = float(input("What is first number?\n"))
    b = float(input("What is second number?\n"))
    result = a * b
    print(f"The result of multiplying {a} and {b} is: {result}")

# function to divide 2 digit number
def divide(a, b):
    a = float(input("What is first number?\n"))
    b = float(input("What is second number?\n"))
    result = a / b
    print(f"The result of dividing {a} and {b} is: {result}")

# 1. TODO - Program greeting 
print("Welcome to simple calculator!")

response = input("What would like to compute. Type add, sub, Mult, div\n")

if response == "add":
    add(a=5, b=5)
elif response == "sub":
    sub(a=5, b=5)
elif response == "mult":
     multiply(a=5, b=5)
elif response == "div":
    divide(a=5, b=5)

else:
    print("Error! Please try again.")
