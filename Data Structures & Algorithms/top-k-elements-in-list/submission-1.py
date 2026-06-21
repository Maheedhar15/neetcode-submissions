class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique = set(nums)
        d = {}
        for i in unique:
            for j in nums:
                if i ==  j:
                    if i not in d.keys():
                        d[i] = 1
                    else:
                        d[i]+=1
        s = sorted(d.items(),key=lambda item: item[1],reverse=True)
        print(s)
        res = []
        for i in range(k):
            res.append(s[i][0])
        return res
        