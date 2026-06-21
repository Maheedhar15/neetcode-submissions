class TimeMap:

    def __init__(self):
        self.TimeMap = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        currList = self.TimeMap.get(key, [])
        currList.append((value, timestamp))
        self.TimeMap[key] = currList
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.TimeMap.get(key, False):
            return ""
        
        times = []
        values = []

        for sets in self.TimeMap[key]:
            times.append(sets[1])
            values.append(sets[0])
        
        res = ""

        l = 0 
        r = len(times) - 1

        while l <= r:
            m = (l + r) // 2

            if times[m] <= timestamp:
                if times[m] == timestamp:
                    res = values[m]
                    break
                else:
                    res = values[m]
                    l = m + 1
            else:
                r = m - 1
        
        return(res)

        
