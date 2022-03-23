a = int(input("Enter a number for a?\n"))
b = int(input("Enter a number for b?\n"))
# before  
print("a is: " + str(a))
print("b is: " + str(b))

c = a
a = b
b = c
# after
print("a is: " + str(a))
print("b is: " + str(b))