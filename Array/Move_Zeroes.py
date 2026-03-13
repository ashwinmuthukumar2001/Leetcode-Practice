
# my first approach
def moveZeroes_(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    if len(nums) == 1:
        return nums

    count = 0
    while 0 in nums and count<len(nums):
        nums.remove(0)
        nums.append(0)
        count+=1

    return nums

# Two Pointer approach -> Optimal
""" 
1) Initially the left pointer starts from the 0th Index and right pointer is used for parsing/scanning the list
2) We skip 0 values and swap non zero values with the left pointer 
3) Left pointer moves 1 step ahead after a swap
"""
def moveZeroes(nums):

    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums

nums = [0,1,0,2,3,0,4,0,8]

print(moveZeroes(nums))
