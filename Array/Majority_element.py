# My first approach using hashmap
def majorityElement_(nums):
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

# Boyer Moore Approach

def majorityElement(nums):
     
    count = 0
    candidate = None

    for i in nums:

        if count == 0:
            candidate = i
         
        if i == candidate:
            count +=1

        else:
            count -=1
    
    return candidate


print(majorityElement([2,2,2,1,1,1,2,2]))