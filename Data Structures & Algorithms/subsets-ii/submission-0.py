class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        def helper(i, nums, curset, subsets):
            n = len(nums)
            if i >= n:
                subsets.append(curset.copy())
                return
            
            curset.append(nums[i])
            helper(i+1, nums, curset, subsets)

            curset.pop()
            helper(i+1, nums, curset, subsets)
        
        subsets, curset = [], []

        helper(0, nums, curset, subsets)

        res = []

        for i in range(len(subsets)):
            if sorted(subsets[i]) not in res:
                res.append(sorted(subsets[i]))
            
        
        return(res)

        