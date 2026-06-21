class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap = [None]
        def push(val):
            self.heap.append(val)
            i = len(self.heap) - 1
            while i > 1 and self.heap[i] < self.heap[i//2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i//2]
                self.heap[i//2] = tmp
                i = i//2
    
        def pop():
            res = self.heap[1]

            self.heap[1] = self.heap.pop()

            i = 1

            while 2*i < len(self.heap):
                if (2 * i + 1 < len(self.heap) and self.heap[2 * i] > self.heap[2 * i + 1] and self.heap[2 * i + 1] < self.heap[i]):
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[2*i] < self.heap[i]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
        
        for val in nums:
            push(val)
            if len(self.heap) > k + 1:
                pop()
        
        return self.heap[1]


        