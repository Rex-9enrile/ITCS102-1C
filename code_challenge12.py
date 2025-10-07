for x in range(1,7,1):
    for y in range(7,x,-1):
        print(" ", end = " ")
    for z in range(x,0,-1):
        print(z, end = " ")
    for a in range(2, x + 1):
        print(a, end = " ")
    print()
