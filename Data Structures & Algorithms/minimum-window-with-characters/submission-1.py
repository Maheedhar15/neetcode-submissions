class Solution:
    from collections import Counter
    import sys
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}
        for i in t:
            countT[i] = 1 + countT.get(i,0)
        res, resLen = [-1,-1], float('inf')

        have,need = 0, len(set(t))
        L= 0
        for R in range(len(s)):
            
            window[s[R]] = 1 + window.get(s[R],0)

            if s[R] in countT and window[s[R]] == countT[s[R]]:
                have+=1
            while have==need:
                if (R - L + 1) < resLen:
                    res = [L,R]
                    resLen = R - L + 1

                window[s[L]] -= 1
                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have-=1
                L+=1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""
                





        