class Solution:
    from collections import deque
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def bfs(r,c):
            ROWS, COLS = len(grid), len(grid[0])

            q = deque()
            q.append((r,c))
            visit = set()
            visit.add((r,c))

            steps = 0
            while q:
                for _ in range(len(q)):
                    r , c = q.popleft()
                    if grid[r][c] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in visit and grid[nr][nc]!=-1):
                            q.append((nr,nc))
                            visit.add((nr,nc))
                steps+=1
            return INF


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c)
                    
        
        