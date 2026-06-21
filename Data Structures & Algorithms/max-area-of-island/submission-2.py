class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(grid, r, c):
            ROWS, COLS = len(grid), len(grid[0])

            if(min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                return 0
            
            area = 1
            grid[r][c] = 0

            area+=dfs(grid,r+1,c)
            area+=dfs(grid,r-1,c)
            area+=dfs(grid,r,c+1)
            area+=dfs(grid,r,c-1)

            return area
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = dfs(grid,r,c)
                    maxArea = max(maxArea, area)
        
        return maxArea