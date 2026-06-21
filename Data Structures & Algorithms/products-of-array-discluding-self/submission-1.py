class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        val = 1
        for i in range(1,len(nums)):
            val*=nums[i - 1]
            prefix.append(val)
        val = 1
        for j in range(len(nums) - 2,-1,-1):
            val*=nums[j + 1]
            suffix.append(val)
        res = []
        for i in range(len(prefix)):
            res.append(prefix[i] * suffix[len(suffix) - 1 - i])
        return res

            

        