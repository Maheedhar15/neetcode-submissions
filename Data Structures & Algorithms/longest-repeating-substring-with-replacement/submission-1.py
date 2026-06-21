class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        d = {}
        max_freq = 0
        max_size = 0

        for R in range(len(s)):

            d[s[R]] = d.get(s[R],0) + 1

            max_freq = max(max_freq, d[s[R]])

            if (R - L + 1) - max_freq > k:
                d[s[L]]-=1
                L+=1
            
            max_size = max(max_size, R - L + 1)
        
        return max_size

        
        