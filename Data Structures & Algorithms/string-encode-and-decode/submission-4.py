class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s+=str(len(i))
            s+='#'
            s+=i
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        l = []
        #print(s)
        while i < len(s):
            j = i + 1
            while j < len(s):
                if s[j] == '#':
                    break
                j+=1
            length = int(s[i:j])
            #print(length)
            l.append(s[j + 1:j + 1 +length])
            i = j + 1 + length
        return l
        
