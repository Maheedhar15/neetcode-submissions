class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, node1):

        if node1 != self.parent[node1]:
            self.parent[node1] = self.find(self.parent[node1])

        return self.parent[node1]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return True

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p2]+=1
        return False

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq
        minHeap = []

        n = len(points)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                heapq.heappush(minHeap, [dist, i, j])

        mst = []
        pathWeight = 0

        uf = UnionFind(n)

        while len(mst) < n - 1:
            wt, n1, n2 = heapq.heappop(minHeap)

            if not uf.union(n1,n2):
                mst.append((n1,n2))
                pathWeight+=wt
        
        return pathWeight
        