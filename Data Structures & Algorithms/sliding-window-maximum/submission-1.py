class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        windowMax = float('-inf')
        maxInd = -1
        for R in range(len(nums)):
            if nums[R] > windowMax:
                windowMax = nums[R]
                maxInd = R
            
            if R >= k:
                if (R - k) >= maxInd:
                    windowMax = float('-inf')
                    for i in range(maxInd+1,R+1):
                        if nums[i] > windowMax:
                            windowMax = nums[i]
                            maxInd = i
            if R>=k-1:
                res.append(windowMax)
        return res

                
                
        