def factorial(num):
	if num == 1:
		return num
	return num * factorial(num-1)

n = int(input())
nums = []
for x in range(0, n):
	nums.append(int(input()))
	
for val in nums:
	print(factorial(val))
	
