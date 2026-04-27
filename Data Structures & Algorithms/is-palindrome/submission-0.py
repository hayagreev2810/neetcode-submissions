class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        s=s.lower()
        while right>left:
            while left<right and not s[left].isalnum():
                left=left+1
            while left<right and not s[right].isalnum():
                right=right-1


            if(s[left]!=s[right]):
                return False
            right=right-1
            left=left+1 
        return True   
        