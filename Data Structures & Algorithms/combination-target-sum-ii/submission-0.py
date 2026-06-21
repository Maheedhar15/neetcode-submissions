class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def helper(i, curSet, subsets, target):
            if target == 0:
                subsets.append(curSet.copy())
                return
            if target < 0 or i>=len(candidates):
                return
            
            curSet.append(candidates[i])
            helper(i+1,curSet,subsets, target - candidates[i])

            curSet.pop()
            helper(i+1, curSet, subsets, target)

        subsets = []

        helper(0, [], subsets, target)

        res = []
        for i in subsets:
            if sorted(i) not in res:
                res.append(sorted(i))
        
        return(res)
        
        