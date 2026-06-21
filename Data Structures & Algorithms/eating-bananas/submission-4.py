class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        upper_bound = max(piles)

        def check_speed(curr_speed, piles):
            t = 0
            for x in piles:
                t = t + math.ceil(x / curr_speed)
            return t

        res = ''
        
        lower_bound = 1

        while lower_bound <= upper_bound:
            m = (lower_bound + upper_bound) // 2

            if check_speed(m, piles) <= h:
                res = m
                upper_bound = m - 1
            else:
                lower_bound = m + 1
        
        return(res)

        