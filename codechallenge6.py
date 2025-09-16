print ("This is a simulation of ODD numbers")

x = 0
for y in range (0, 10, 1):
    v = eval(input("Enter a number --->   "))
    if v % 2:
     x += v
print (" The sum of all ODD number :",x)