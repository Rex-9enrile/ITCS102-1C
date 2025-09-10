temp = eval(input("Enter Temperature outside --> "))

if temp <= 0:
	print("Temperature is considered as freezing temperature")
elif temp >= 1 and temp <= 20:
	print("The temperature is condsidered extremely cold")
elif temp > 20 and temp <= 30:
	print("Temperature is concidered as cold")
elif temp > 31 and temp <= 37:
	print("Temperature is considered as lukewarm")
elif temp > 38 and temp <= 45:
	print("Temperature is considered as hot")
elif temp > 45 and temp <= 50:
	print("Temperature is considered as boiling hot")
elif temp > 51 and temp <= above:
	print("Temperature is considered as dangerous temperature")
else: 
	print("Temperature Invalid") 	