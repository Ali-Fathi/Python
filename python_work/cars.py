# Sorting a list Permanently with the sort() Method
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

# Sorting s List Temporarily with the sorted() Function
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print("Here is the original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original list again:")
# print(cars)

# Printing a List in Reverse order

cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)

# cars.reverse()
# print(cars)
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

