class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two Pointers method
        left, right = 0, len(heights) - 1
        maxWater, currWater = 0, 0
        while left < right:
            length = right - left
            h = min(heights[left], heights[right])
            currWater = length * h
            maxWater = max(maxWater, currWater)
            if (heights[left] < heights[right]):
                left+=1
            else:
                right-=1
        return maxWater

                

        