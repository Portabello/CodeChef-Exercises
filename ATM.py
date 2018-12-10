import re
print("*ATM*")
balance = None
while True:
	x = input()
	x = x.split()
	withdrawl = int(x[0])
	balance = float(x[1])
	if withdrawl > balance:
		#print("INSUFFICIENT FUNDS!")
		break
	elif withdrawl % 5 == 0:
		balance = balance - withdrawl - 0.5
		#print("WITHDRAWL SUCCESS!!")
		break
	else:
		#print("INVALID WITHDRAWL!!!")
		break
#print("CURRENT ACCOUNT BALANCE: $", "{:.2f}".format(balance))
print("{:.2f}".format(balance))