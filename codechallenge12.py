for n in range(1, 7, 1):
    for t in range(7, n, -1):
        print(" ", end=" ")
    for a in range(n, 0, -1):
        print(a, end=" ")
    for e in range(2, n+1, 1):
        print(e, end=" ")
    print("")