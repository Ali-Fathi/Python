#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)
# Changes honda -> to ducati
#motorcycles[0] = 'ducati'
#print(motorcycles)

# Adding elements to a list
#motorcycles.append('ducati')
#print(motorcycles)


motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

#print(motorcycles)

# Inserting element to a list
motorcycles.insert(0, 'ducati')
#print(motorcycles)

# Removing an item Using the del Statement
#del motorcycles[0]
#print(motorcycles)

# Removing an Item Using the pop() Method
#popped_motorcycles = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycles)

#motorcycles = ['honda', 'yamaha', 'suzuki']
#last_owned = motorcycles.pop()

#first_owned = motorcycles.pop(0)
#print(f"The last motorcyle I owned was a {first_owned .title()}.")

# Removing an Item by Value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
