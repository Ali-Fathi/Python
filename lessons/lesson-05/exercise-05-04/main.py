# TODO 1. Ddeclare range of numbers between 1 and 100

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 5 == 0:
    print("Fizz")
  elif number % 3 == 0:
    print("Buzz")
  else:
    print(number)