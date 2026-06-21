class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        hashmap_s1 = {}

        for i in s1:
            if i not in hashmap_s1:
                hashmap_s1[i] = 1
            else:
                hashmap_s1[i]+=1
        
        L,R = 0,0
        hashmap_s2 = {}
        while R < len(s2):
            if (R - L + 1) > len(s1):
                hashmap_s2[s2[L]]-=1
                if hashmap_s2[s2[L]] == 0:
                    del hashmap_s2[s2[L]]
                L+=1
                if s2[R] in hashmap_s2:
                    hashmap_s2[s2[R]]+=1
                else:
                    hashmap_s2[s2[R]] = 1
            else:
                if s2[R] in hashmap_s2:
                    hashmap_s2[s2[R]]+=1
                else:
                    hashmap_s2[s2[R]] = 1
            if hashmap_s2 == hashmap_s1:
                return True
            R+=1
        
        return False
            
                

        