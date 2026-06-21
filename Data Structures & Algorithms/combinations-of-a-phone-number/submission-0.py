class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}

        #print(hashmap)
        n = len(digits)
        def helper(i, curString, res, n):
            if n == 0:
                return
            if i == n:
                res.append(curString)
                return
            
            for ind in range(len(hashmap[digits[i]])):
                curString+=hashmap[digits[i]][ind]
                helper(i+1, curString, res, n)
                curString = curString[:-1]
        
        res = []
        helper(0, "", res, n)
        return(res)



        