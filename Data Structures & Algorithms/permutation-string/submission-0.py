class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        src_len = len(s1)

        substr = s2[0:src_len]

        if sorted(substr) == sorted(s1):
            return True

        for r in range(len(s2) - src_len):
            substr = substr[1:] + s2[r+src_len]
            if sorted(substr) == sorted(s1):
                return True
        
        return False
            
        