class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
            
        stretch1 = nums[:n-1]
        stretch2 = nums[1:n]

        hashmap = {}

        def dfs(i, arr):
            if i >= len(arr):
                return 0
            if i in hashmap:
                return hashmap[i]
            
            hashmap[i] = max(arr[i] + dfs(i+2, arr), dfs(i+1,arr))
            return hashmap[i]

        val1 = dfs(0, stretch1)
        hashmap = {}
        val2 = dfs(0,stretch2)
        return max(val1,val2)

        