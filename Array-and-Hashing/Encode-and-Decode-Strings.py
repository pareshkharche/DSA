#Encode and Decode Strings
from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=[]
        for s in strs:
            ans.append('{:4}'.format(len(s)) + s)
        return ''.join(ans)

    def decode(self, s: str) -> List[str]:
        ans=[]
        i,n = 0,len(s)
        while i<n:
            size=int(s[i : i + 4])
            i += 4
            ans.append(s[i : i + size])
            i += size
        return ans

dummy_input = ["Hello", "World"]

sol = Solution()

# Encode
encoded = sol.encode(dummy_input)
print("Encoded:", encoded)

# Decode
decoded = sol.decode(encoded)
print("Decoded:", decoded)