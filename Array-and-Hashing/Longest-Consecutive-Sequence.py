#Longest consecutive sequence

#nums=[1,99,101,98,2,5,3,100,1,1]

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set=set()
        n=len(nums)
        for i in range(0, n):
            my_set.add(nums[i])
            
        longest=0
        for num in my_set:
            if num-1 not in my_set:
                x=num
                count=1
                while x+1 in my_set:
                    count+=1
                    x+=1
                longest=max(longest, count)
                
        return longest
    

nums=[2,20,4,10,3,4,5]
sol=Solution()
print(sol.longestConsecutive(nums))

# TC:O(n+n+n) : O(3N)
# SC:O(N)