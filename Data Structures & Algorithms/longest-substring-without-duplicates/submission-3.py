class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = 0
        i = 0
        # if s == " ":
        #     return 1
        while i < len(s):
            substr = s[i]
            curr = 1
            j = i + 1
            while j < len(s):
                if s[j] not in substr:
                    substr+=s[j]
                    curr += 1
                    j+=1
                else:
                    break
            size = max(size,curr)
            i+=1
        return size
            

        