class Solution:
    import heapq
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        def dikstra(edges, n, src):
            adj = {}

            for i in range(1,n+1):
                adj[i] = []
            
            for s,d,w in edges:
                adj[s].append([d,w])

            shortest = {}

            minHeap = [[0,src]]

            while minHeap:
                d1, n1 = heapq.heappop(minHeap)
                if n1 in shortest:
                    continue
                shortest[n1] = d1

                for n2, d2 in adj[n1]:
                    if n2 not in shortest:
                        heapq.heappush(minHeap, (d1 + d2, n2))
            
            return shortest
        
        shortest = dikstra(times, n ,k)

        flag = False
        maxVal = float('-inf')
        for i in range(1, n+1):
            if i not in shortest:
                flag = True
            else:
                maxVal = max(maxVal, shortest[i])
        
        if flag:
            return -1
        else:
            return maxVal
            
        

        