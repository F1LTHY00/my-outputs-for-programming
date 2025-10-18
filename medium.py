col = eval(input("Enter a number of columns ===> "))

for i in range (1, 11, 1):
    for p in range (1, col+1, 1):
        print (f"{i} x {p} = {p * i}", end="\t")
    print( )

for i in range (1, 7, 1):
    for x in range (7, i, -1):
        print (" ", end="")
    for y in range (1, i, 1):
        print ("* ", end="")
    print ( )