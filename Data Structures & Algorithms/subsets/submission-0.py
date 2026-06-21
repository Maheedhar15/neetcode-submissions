class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def helper(ind, nums, curset, subsets):
            if ind >= len(nums):
                subsets.append(curset.copy())
                return
            
            curset.append(nums[ind])
            helper(ind + 1, nums, curset, subsets)

            curset.pop()
            helper(ind + 1, nums, curset, subsets)

        subsets, curset = [], []
        helper(0, nums, curset, subsets)
        return subsets    

        