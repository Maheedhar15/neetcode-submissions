class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r,c,visit, word, currStr):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visit or len(currStr) == len(word):
                if currStr == word:
                    return True
                else:
                    return False
            
            visit.add((r,c))

            currStr+=board[r][c]
            print(currStr, r,c)

            for dr,dc in directions:
                flag = dfs(r + dr, c + dc, visit, word, currStr)
                if flag:
                    return True
            
            visit.remove((r,c))
                
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    flag = dfs(r,c,set(),word,'')
                    if flag:
                        return True

        return False
        

        