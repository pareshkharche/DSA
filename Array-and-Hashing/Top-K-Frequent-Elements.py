
# from typing import List
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count={}
#         freq=[[] for i in range(len(nums) + 1)]
#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
#         for n, c in count.items():
#             freq[c].append(n)
        
#         res=[]
#         for i in range(len(freq) - 1, 0 ,-1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res
                
# nums = [1,2,2,3,3,3]
# k=2
# sol=Solution()
# result=sol.topKFrequent(nums,k)
# print(result)


from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Step 1: Count frequency
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Step 2: Use min heap
        heap = []
        
        for n, freq in count.items():
            heapq.heappush(heap, (freq, n))
            
            # Keep only k elements
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Step 3: Extract result
        res = []
        for freq, n in heap:
            res.append(n)
    
        return res


# 🔹 Hardcoded input
nums = [1, 2, 2, 3, 3, 3]
k = 2

sol = Solution()
print(sol.topKFrequent(nums, k))