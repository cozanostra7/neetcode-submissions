class Solution:
    def isPalindrome(self, s: str) -> bool:
        myStr = ''

        for c in s:
            if c.isalnum():
                myStr+=str(c).lower()
        return myStr == myStr[::-1]


        