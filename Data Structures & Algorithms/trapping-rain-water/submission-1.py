class Solution:
    import sys
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        left_max, right_max = height[L], height[R]
        maxSum = 0
        while L<R:
            if left_max < right_max:
                L+=1
                left_max = max(left_max, height[L])
                maxSum+=max(0,left_max - height[L])
            else:
                R-=1
                right_max = max(right_max, height[R])
                maxSum+=max(0,right_max - height[R])
        return maxSum


                    
        