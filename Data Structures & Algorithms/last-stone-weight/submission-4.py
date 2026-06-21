class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = []

        def helper(i,n):
            while 2 * i <= n:
                largest = i
                left = 2 * i
                right = 2 * i + 1

                if left < n and self.heap[largest] < self.heap[left]:
                    largest = left

                if right < n and self.heap[largest] < self.heap[right]:
                    largest = right
                
                if largest != i:
                    self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                    i = largest
                else:
                    break

        def heapify(arr):
            self.heap = [None] + arr

            n = len(self.heap)

            for cur in range((n // 2), 0, -1):
                helper(cur, n)
        
        heapify(stones)
        #print(self.heap)

        def remove():
            if len(self.heap) == 2:
                return self.heap.pop(1)
            res = self.heap[1]

            self.heap[1] = self.heap.pop()

            i = 1

            helper(i,len(self.heap))

            return res
        
        def push(val):

            self.heap.append(val)
            i = len(self.heap) - 1

            while i > 1 and self.heap[i] > self.heap[i//2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i//2]
                self.heap[i//2] = tmp
                i = i // 2

        while len(self.heap) > 2:
            first = remove()
            second = remove()

            if first == second:
                if len(self.heap) == 1:
                    push(0)
                else:
                    pass
            else:
                if first - second > 0:
                    push((first - second))
                else:
                    push((second - first))
        return(self.heap[1])



        





        


        