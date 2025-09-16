x = eval(input("Enter a number ===>   "))
factorial = 1
for y in range (x, 0, -1):
     factorial *= y 
print (" The Factorial of", x, "is", factorial)