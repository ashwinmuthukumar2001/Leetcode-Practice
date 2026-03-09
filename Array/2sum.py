# Hash map approach
nums = [4,7,2,1,3]
temp = {} 
target = 9


for i in range(0,len(nums)):
	
	b = target - nums[i]
	
	if b in temp: # check if value already exists in the dictionary
		print([temp[b], i])
	else:
		temp[nums[i]] = i