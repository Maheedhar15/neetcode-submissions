class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        window1 = dict(Counter(s1))

        k = len(s1)

        if len(s2) < k:
            return False

        l = 0
        window = dict()

        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1

            if ((r - l) + 1) == k:
                if window == window1:
                    return True

            if ((r - l) + 1) > k:
                window[s2[l]]-=1

                if window[s2[l]] == 0:
                    del window[s2[l]]

                if window == window1:
                    return True

                l+=1
    
        return False
        