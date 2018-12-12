t = int(input())
for x in range(0, t):
	num = input()
	count4 = 0
	for y in range(0, len(num)):
		if num[y] == '4':
			count4 += 1
	print(count4)