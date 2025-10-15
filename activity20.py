hot = True

while hot == True:
    still_hot = input("It is still hot (yes/no) --> ").lower()

    if still_hot == "yes":
        print("Make it cold ...")
        continue
    else:
        print("oh it's hot ...")
        break