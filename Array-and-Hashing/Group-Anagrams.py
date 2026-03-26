from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for s in strs:
            count = [0] * 26
            
            for letter in s:
                count[ord(letter) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
    
strs = ["eat","tea","tan","ate","nat","bat"]
sol=Solution()
result=sol.groupAnagrams(strs)
print(result)


#Time complexity: O(NK) and Space Complexity: O(NK)
# N=Number of strings
# K=maximum length of a string
