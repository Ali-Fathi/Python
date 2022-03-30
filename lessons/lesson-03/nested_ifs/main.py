height = int(input("Enter your height in cm? "))

if height > 120:
  print("You can ride rollercoaster!")
  age = int(input("Enter your age? "))
  if age > 18:
    print("your ticket price is: $12")
  elif age < 18:
    print("Your ticket price is: $7")
  else:
    print("Enter under or over 18 number for your age!")
else:
  print("Sorry, you have to grow taller before you can ride rollercoaster.")