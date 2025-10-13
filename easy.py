for i in range (1,6,1):
    for x in range (6, i, -1):
        print(" ", end = " ")
    for p in range (1, i*2, 1):
        print ("*", end = " ")

    print ( )


for i in range (1,6,1):
    for q in range (1, i+1,1):
        print (i, end = " ")
    print ( )