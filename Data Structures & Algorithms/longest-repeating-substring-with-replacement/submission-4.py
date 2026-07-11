class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hd={}
        length=0
        l=0
        for r in range(len(s)):
            hd[s[r]]=hd.get(s[r],0)+1 
            subtr_len=(r-l)+1
            rep_char=subtr_len-max(hd.values())
            if rep_char>k:
                hd[s[l]]=hd.get(s[l],1)-1
                l=l+1
            else:
                length=max(subtr_len,length)
        return length



