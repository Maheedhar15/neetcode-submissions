class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        adj_list = defaultdict(list)

        if len(edges) >= n:
            return False

        for node, conn in edges:
            adj_list[node].append(conn)
            adj_list[conn].append(node)

        visited = set([0])

        q = deque([0])

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
        
        return len(visited) == n
         

        