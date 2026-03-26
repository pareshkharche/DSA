class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict={}
        t_dict={}
        
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
            
        return s_dict  == t_dict
    
# 🔹 Hardcoded input (Example 1)
s = "anagram"
t = "nagaram"

sol = Solution()
print(sol.isAnagram(s, t))


# Time complexity :O(n) and space complexity: O(n)