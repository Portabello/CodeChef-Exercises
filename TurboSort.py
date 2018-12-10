def bubbleSort(nums):
	swap = False
	for x in range(0, len(nums)-1):
		if nums[x] > nums[x+1]:
			nums[x], nums[x+1] = nums[x+1], nums[x]
			swap = True
	if swap == True:
		bubbleSort(nums)
	return nums

t = int(input())
nums = []
for x in range(0, t):
	nums.append(int(input()))
nums = bubbleSort(nums)

for vals in nums:
	print(vals)