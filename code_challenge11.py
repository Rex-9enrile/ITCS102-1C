
for i in range(1, 11, 1):
    for a in range(10, i, -1):
        print(" ", end = " ")
    for b in range(1, i, 1):
        print("*", end = " ")
    for c in range(1, i, 1):
        print("*", end = " ")
    print()