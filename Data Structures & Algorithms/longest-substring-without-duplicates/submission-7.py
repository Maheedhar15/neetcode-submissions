class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = 0
        L = 0
        hashset = set()
        
        for R in range(len(s)):
            
            while s[R] in hashset:
                hashset.remove(s[L])
                L+=1
            
            else:
                hashset.add(s[R])
            size = max(size, (R-L+1))
        return size
            

        