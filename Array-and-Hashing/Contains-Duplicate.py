#217. Contains Duplicate
'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.
'''
# APPROACH: Hash Set  |  TC: O(n)  |  SC: O(n)

from typing import List
# def containsDuplicate(nums):
#     seen = set()
#     for n in nums:
#         if n in seen:
#             return True
#         seen.add(n)
#     return False




# if __name__ == "__main__":
#     # Test 1 - has duplicate → True
#     print(containsDuplicate([1, 2, 3, 1]))      

#     # Test 2 - no duplicate → False
#     print(containsDuplicate([1, 2, 3, 4]))       

#     # Test 3 - all same → True
#     print(containsDuplicate([1, 1, 1, 1]))       

#     # Test 4 - single element → False
#     print(containsDuplicate([99]))        
    
    
    
# APPROACH 1: Brute Force  |  TC: O(n²)  |  SC: O(1)

def containsDuplicate_brute(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


if __name__ == "__main__":
    print(containsDuplicate_brute([1, 2, 3, 1]))   # True
    print(containsDuplicate_brute([1, 2, 3, 4]))   # False
    print(containsDuplicate_brute([1, 1, 1, 1]))   # True
    print(containsDuplicate_brute([99]))            # False