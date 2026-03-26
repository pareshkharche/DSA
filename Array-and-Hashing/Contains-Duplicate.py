# APPROACH: Hash Set  |  TC: O(n)  |  SC: O(n)
from typing import List
def containsDuplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


if __name__ == "__main__":
    print(containsDuplicate([1, 2, 3, 1]))      
    print(containsDuplicate([1, 2, 3, 4]))             
    
# APPROACH 1: Brute Force  |  TC: O(n²)  |  SC: O(1)

# def containsDuplicate_brute(nums):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False


# if __name__ == "__main__":
#     print(containsDuplicate_brute([1, 2, 3, 1]))   
#     print(containsDuplicate_brute([1, 2, 3, 4]))   
#     print(containsDuplicate_brute([1, 1, 1, 1]))   
#     print(containsDuplicate_brute([99]))            