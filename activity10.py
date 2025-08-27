from getpass import getpass

username = 'rex' 
pword = 'enrile09'

u = input("USERNAME --> ")
p = getpass("PASSWORD --> ")

if (u == username) and (p == pword) :
	print("Access Granted")
else:
	print("Accesss Denied")