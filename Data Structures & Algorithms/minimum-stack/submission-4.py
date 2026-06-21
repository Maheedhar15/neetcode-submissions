class MinStack:
    import sys
    def __init__(self):
        self.l = []
        self.t = None
        self.minEle = sys.maxsize
        

    def push(self, val: int) -> None:
        self.l.append(val)
        if self.t == None:
            self.t = 0
            self.minEle = val
        else:
            if val < self.minEle:
                self.minEle = val
            self.t+=1

    def pop(self) -> None:
        _ = self.l.pop()
        if self.l != []:
            self.minEle = min(self.l)
        else: self.minEle = sys.maxsize
        self.t-=1

    def top(self) -> int:
        return self.l[self.t]
        

    def getMin(self) -> int:
        return self.minEle
        
