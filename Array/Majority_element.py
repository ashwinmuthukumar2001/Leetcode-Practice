def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = {}

        if len(nums) == 1:
            return nums

        for i in nums:

            if i in temp:
                temp[i]  += 1
                if temp[i] > len(nums)/2:
                    return i
            else:
                temp[i] = 1

print(majorityElement([2,2,2,1,1,1,2,2]))