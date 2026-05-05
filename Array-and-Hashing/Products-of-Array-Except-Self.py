# class Solution:
#     def productExceptSelf(self, nums):
#         n=len(nums)
#         result= [0] * n
#         for i in range(n):
#             product=1
#             for j in range(n):
#                 if i != j:
#                     product *= nums[j]  
#             result[i] = product
#         return result
    
#tc:O(n^2) Sc:O(1)


#optimized solution
class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        result=[1]*n
        
        #prefix
        prefix=1
        for i in range(n):
            result[i]=prefix
            prefix *= nums[i]
            
        #suffix 
        suffix=1
        for i in range(n-1,-1,-1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
    
#TC:O(n)  Sc:O(1)
        
nums=[1,2,4,6]
sol=Solution()
print(sol.productExceptSelf(nums))
