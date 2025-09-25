#part 1

a = 'sam'
b = 'bading'

print (f"Is this what you wanted to say ({a} {b}) ?" ) 

#part 2

number = 10

print("Input Ten (10) numbers to add to the number 10")

for i in range(1, 11, 1):
    x = eval(input(f"{i} - Input the number here --> "))
    number += x
print(f"This is the total ({number})")