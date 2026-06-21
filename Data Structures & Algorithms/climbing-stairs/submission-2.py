class Solution:
    def climbStairs(self, n: int) -> int:
        hashmap = {1:1, 2:2}

        def recur(n, hashmap):
            if n in hashmap:
                return hashmap[n]
            
            hashmap[n] = recur(n-1, hashmap) + recur(n-2, hashmap)

            return hashmap[n]
        return recur(n, hashmap)
        
        