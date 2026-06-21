class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        res = []
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            n = arr[i]
            l,r = i+1, len(arr) - 1
            while l < r:
                if n + arr[l] + arr[r] > 0:
                    r-=1
                elif arr[l] + arr[r] + n < 0:
                    l+=1
                else:
                    ak = sorted([n,arr[l],arr[r]])
                    if ak not in res:
                        res.append(ak)
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res
        