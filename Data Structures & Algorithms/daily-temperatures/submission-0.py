class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = 0
        n = len(temperatures)
        res = [0] * n
        while l < n:
            for r in range(l+1,n):
                if temperatures[r] > temperatures[l]:
                    res[l] = (r-l)
                    break
            l+=1
        return res

        