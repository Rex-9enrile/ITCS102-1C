name = input("What is your name --> ")
print("\n++++++++++++++++++++++++++++++++++++++++++++")
print("\nODD NUMBER SELECTOR, press o to stop the loop")
print("\n++++++++++++++++++++++++++++++++++++++++++++")

tuloy = True
sum = 0
even = "" 

while tuloy == True:
    oddnum = eval(input("\ninput a random number --> "))

    if oddnum % 2 == 1:
        print("ODD NUMBER DETECTED")
        sum += oddnum
        even += str(oddnum) + " "       
        continue

    elif oddnum == 0:
        print("loop teminated")
        break

    else:
        if oddnum % 2 == 0:
            print("EVEN NUMBER DETECTED")
            continue

        else: 
            print("please input a valid number")
        continue

print(f"Hi {name}, the sum off all ADD numbers is {sum}")
print(f"ODD numbers includethe ff -> {even}")