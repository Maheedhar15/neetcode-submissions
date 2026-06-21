class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance_heuristic(pt):
            return (pt[0] ** 2 + pt[1] ** 2)

        def helper(i,n):
            while 2 * i < n:
                smallest = i
                left = 2 * i
                right = 2 * i + 1
                

                if left < n and distance_heuristic(self.heap[left]) < distance_heuristic(self.heap[smallest]):
                    smallest = left
                
                if right < n and distance_heuristic(self.heap[right]) < distance_heuristic(self.heap[smallest]):
                    smallest = right
                
                if smallest != i:
                    self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                    i = smallest
                else:
                    break

        
        def heapify(arr):

            self.heap = [None] + arr

            n = len(self.heap)

            for i in range((n//2),0,-1):
                helper(i, n)

        def remove():
            if len(self.heap) == 2:
                return self.heap.pop()

            res = self.heap[1]

            self.heap[1] = self.heap.pop()

            helper(1,len(self.heap))

            return res
        
        heapify(points)

        print(self.heap)
        l = []

        for i in range(k):

            l.append(remove())
        
        return(l)




        