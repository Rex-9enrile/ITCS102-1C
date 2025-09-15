
print("Welcome to manga reader recommander")
print("Please answer a few questions to proceed ")

x = input("are you interested? yes/no")

if x. lower() == "yes":
    anime = input("what genre do you seem to be interested with: comedy/action/horror \n").lower()
    decade = input("what decades range of manga do you want to read:1 (1990s) , 2 (2000s) \n").lower()
    L = input("How long do you want to read a kind of manga: 1 (long) , 2 (short) /n").lower()

if anime == "comedy" and decade == '1' and L == '1':
    print("i would highly recommend this to you (great teacher onizuka)")
elif anime == "comedy" and decade =='2'and L == '2':
      
      print("i would highly recommend this to you (yakitate japan)")
elif anime == "action" and decade == '1' and L == '1':
      print("i would like highly recommend this to you (hunter x hunter)")
elif anime == "action" and decade == '2' and L == '2':
     print("i would highly recommend this to you (death note)")
elif anime == "horro" and decade == '1' and L == '1':
     print("i would highly recommend this to you (berserk)")
elif anime == "horror" and decade == '2' and L == '2':
     print("i would highly recommend this to you (tokyo ghoul")
else:
     print("sorry, i don't have other type of genre that i could reccomend to you, sorry")

     print("okay thank you,come back of you're interested in reading manga")
     

      
