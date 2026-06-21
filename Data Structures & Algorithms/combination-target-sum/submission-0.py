class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def helper(i, curset, subsets, target):
            if target == 0:
                subsets.append(curset.copy())
                return
            if target < 0 or i >= len(nums):
                return
            
            newTarget = target - nums[i]
            curset.append(nums[i])
            helper(i, curset, subsets, newTarget)

            curset.pop()
            helper(i + 1, curset, subsets, target)

        subsets = []

        helper(0, [], subsets, target)
        
        return(subsets)
        