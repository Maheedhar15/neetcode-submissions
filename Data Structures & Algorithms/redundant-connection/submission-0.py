class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class UnionFind:
            def __init__(self, n):
                self.par = {}
                self.rank = {}

                for i in range(1,n+1):
                    self.par[i] = i
                    self.rank[i] = 0
            
            def find(self, n):
                if n != self.par[n]:
                    self.par[n] = self.find(self.par[n])
                return self.par[n]
            
            def union(self, n1, n2):
                p1 = self.find(n1)
                p2 = self.find(n2)

                if p1 == p2:
                    return False
                
                if self.rank[p1] > self.rank[p2]:
                    self.par[p2] = p1
                elif self.rank[p2] > self.rank[p1]:
                    self.par[p1] = p2
                else:
                    self.par[p1] = p2
                    self.rank[p2]+=1
                
                return True
        
        n = 0
        for i in edges:
            n = max(n, max(i))
        
        union_tree = UnionFind(n)

        for n1, n2 in edges:
            if not union_tree.union(n1,n2):
                return [n1, n2]
        

        