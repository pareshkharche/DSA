from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Bruteforce
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []

        num_to_index={}
        for i,num in enumerate(nums):
            complement = target-num
            if complement in num_to_index:
                return [num_to_index[complement],i]
            
            num_to_index[num]=i
        return []
    
if __name__ == "__main__":
    nums=[3,4,5,6]
    target=7
    sol=Solution()
    result=sol.twoSum(nums, target)
    print("Output: ", result)
        