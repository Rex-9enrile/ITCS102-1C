name = input("Input your name --> ")

amount = input("How much is your fee?  ")
discount = amount % 20
sname = input("Are you a student?   ")

Y = 'yes'
N = 'no'

if Y == 'yes' :
	eval(input("Your discount is", discount))
else:
	print("Still", amount)
	
