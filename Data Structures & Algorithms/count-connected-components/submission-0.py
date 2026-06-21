class Solution:
    from collections import deque
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = {i:False for i in range(n)}
        adj_list = {i:[] for i in range(n)}

        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        def bfs(i,adj_list):
            if visited[i]:
                return 0
            
            q = deque()
            q.append(i)

            while q:
                node = q.popleft()
                visited[node] = True
                for neighbor in adj_list[node]:
                    if not visited[neighbor]:
                        q.append(neighbor)
            
            return 1
        count = 0
        for i in range(n):
            count+=bfs(i, adj_list)
        return(count)
        

            
        