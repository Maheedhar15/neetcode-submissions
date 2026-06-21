class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import deque
        adj_list = dict()

        for i in range(len(equations)):
            start, end = equations[i]

            l1 = adj_list.get(start, [])
            l2 = adj_list.get(end, [])

            l1.append((end, values[i]))
            l2.append((start, (1/values[i]) ))

            adj_list[start] = l1
            adj_list[end] = l2

        def bfs(start, target):
            curr = 1

            q = deque()

            q.append((start, curr))

            visited = set()
            visited.add(start)

            while q:
                for _ in range(len(q)):
                    node, val = q.popleft()
                    visited.add(node)

                    if node not in adj_list:
                        return -1.0

                    if node == target:
                        return val

                    for neighbour, mult in adj_list[node]:
                        if neighbour not in visited:
                            q.append((neighbour, val * mult))
                        

            return -1.0

        res = []

        for start, target in queries:
            res.append(bfs(start, target))

        return res
        