class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=0
        r=len(s)-1
        while l<r:
            while l<r and s[l].isalnum()==False :
                l=l+1
            while r>l and  s[r].isalnum()==False :
                r=r-1
            if(s[l]!=s[r]):
                return False
            l=l+1
            r=r-1
        return True
