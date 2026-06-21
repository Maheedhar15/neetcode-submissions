class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = {}

        def recur(i, rob):
            if i >= len(nums):
                return 0
            if i in rob:
                return rob[i]
            
            rob[i] = max(nums[i] + recur(i+2, rob), recur(i+1, rob))
            return rob[i]
        return recur(0,rob)

        