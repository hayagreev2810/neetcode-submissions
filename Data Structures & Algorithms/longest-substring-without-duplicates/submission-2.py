class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hd={}
        l=0
        length=0
        for r in range (len(s)):
            if s[r] not in hd:
                hd[s[r]]=hd.get(s[r],0)+1
                str_len=(r-l)+1
                length=max(length,str_len)
            else:
                while s[r] in hd:
                    del hd[s[l]]
                    l=l+1
                hd[s[r]]=hd.get(s[r],0)+1
               
        return length
