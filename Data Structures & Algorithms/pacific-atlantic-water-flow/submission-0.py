class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        ROWS,COLS = len(heights), len(heights[0])
        def dfs(r,c,visit):
            visit.add((r,c))

            for dr,dc in directions:
                nr,nc = r + dr, c + dc

                if(0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in visit and heights[nr][nc] >= heights[r][c]):
                    dfs(nr,nc,visit)

        pacific, atlantic = set(), set()
        top,bottom = 0,len(heights) - 1
        left,right = 0, len(heights[0]) - 1

        for r in range(top,bottom + 1):
            dfs(r,left,pacific)
            dfs(r,right,atlantic)
        
        for c in range(left, right + 1):
            dfs(top,c,pacific)
            dfs(bottom,c,atlantic)

        res = list(pacific & atlantic)

        res = [list(cell) for cell in res]

        return res
        









        