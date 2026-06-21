class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s+=str(len(i))+":"+i
        return s


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find(':',i)
            length = int(s[i:j])
            i = j+1
            res.append(s[i:i+length])
            i+=length
        return res