class Solution:
    
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        import heapq
        adj_list = {i: [] for i in range(n)}

        for u,v,w in edges:
            adj_list[u].append((v,w))

        def dijkstras(n, adj_list, src):
            distances = [float('inf') for i in range(n)]
            visited = [False for i in range(n)]

            distances[src] = 0

            minHeap = [(0, src)]

            while minHeap:

                node_distance, node = heapq.heappop(minHeap)

                if visited[node]:
                    continue
                
                visited[node] = True

                for neighbour, dist in adj_list[node]:
                    new_distance = dist + node_distance
                    if new_distance < distances[neighbour] and not visited[neighbour]:
                        distances[neighbour] = new_distance
                        heapq.heappush(minHeap, (new_distance, neighbour))
            
            return(distances)
        
        distances = dijkstras(n, adj_list, src)

        res = {}

        for i in range(n):
            res[i] = distances[i] if distances[i] != float('inf') else -1
        
        return res

