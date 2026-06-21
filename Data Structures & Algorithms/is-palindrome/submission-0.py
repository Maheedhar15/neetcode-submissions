class Solution:
    def isPalindrome(self, s: str) -> bool:
        st= ''
        for i in s:
            if i.isalnum():
                st+=i.lower()
        return st == st[::-1]
        