class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ''

        for i in strs:
            s+=str(len(i))
            s+=":"
            s+=i
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        l = []
        while i < len(s):
            j = s.find(":",i)
            k = int(s[i:j])
            ak = s[j+1 : j + 1 + k]
            l.append(ak)
            i = j + 1 + k
        
        return l
