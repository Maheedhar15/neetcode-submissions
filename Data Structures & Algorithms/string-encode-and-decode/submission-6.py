class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for st in strs:
            s+=str(len(st))
            s+=':'
            s+=st
        return(s)

    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        res = []
        while i <= len(s) - 1:
            j = s.find(':', i)
            length = int(s[i:j])
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return res

