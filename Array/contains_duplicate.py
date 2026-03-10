
# Pythonic Approach
def containsDuplicate_(nums):
    return len(nums) != len(set(nums))

# Hash set approcah
def containsDuplicate(nums):

        seen = set() # We use set because retrieval of elements in set is very fast compared to list
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i) # Set does not store duplicates values

        return False

nums = [1,1,1,3,3,4,3,2,4,2]

print(containsDuplicate(nums))