import random

print("\n NUMBER GUESSING GAME")
print("\n+++++++++++++++++++++")

random_value = random.randint(1,5)
tries = 0
tuloy = True

name = input("input your name --->")

while tuloy == True:
    num = eval(input("guess the number 1 to 5 --> "))
    tries += 1
    if num == random_value:
        print("winner !!!!")
        break
    else:
        print("incorrect guess")
        continue

print(f"Hi {name}, your guess is correct, number of tries {tries}")