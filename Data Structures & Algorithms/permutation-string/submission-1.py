class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        src_len = len(s1)
        # Sorting takes time, so using character frequency counter
        substr = Counter(s2[0:src_len])

        src_char_counter = Counter(s1)

        if substr == src_char_counter:
            return True

        for r in range(src_len, len(s2)):
            substr[s2[r]]+=1

            substr[s2[r - src_len]]-=1
            if substr[s2[r - src_len]] == 0:
                del substr[s2[r - src_len]]

            if substr == src_char_counter:
                return True
        
        return False
            
        