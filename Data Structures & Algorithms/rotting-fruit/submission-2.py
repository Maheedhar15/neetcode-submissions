class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:

        visit = set()
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
        
        def bfs():

            ROWS, COLS = len(grid), len(grid[0])
            if q:
                visit.add(q[0])
            length = -1

            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            while q:
                print(q)
                for i in range(len(q)):
                    r, c = q.popleft()
                    
                    for dr, dc in directions:
                        r1, c1 = r + dr, c + dc
                        if (min(r1,c1) < 0 or r1 >= ROWS or c1 >= COLS or (r1,c1) in visit or grid[r1][c1] != 1):
                            continue
                        grid[r1][c1] = 2
                        visit.add((r1,c1))
                        q.append((r1,c1))
                length+=1
            
            return length

        length = bfs()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1 

        if length == -1:
            return 0
        else:
            return length
        