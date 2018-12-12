import sys
#python sets limits on recursion depth, this limits the input to 1498
sys.setrecursionlimit(1500)

def factorial(n):
	if n == 1:
		return n
	return n * factorial(n-1)
	
def zeroCounter(n):
	count = 0
	for x in range(len(n)-1,0, -1):
		if n[x] == '0':
			count += 1
		else:
			break
	return count
	
t = int(input())
for x in range(0,t):
	num = int(input())
	print(zeroCounter(str(factorial(num))))