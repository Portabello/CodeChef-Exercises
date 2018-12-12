def reverse(s):
	str = ""
	for x in s:
		str = x + str
	return str

t = int(input())
for x in range(0, t):
	print(reverse(input()))

