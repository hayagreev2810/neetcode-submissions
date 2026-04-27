class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        hd={}
        for i in range(len(s)):
            if s[i] in hd:
                hd[s[i]]=hd[s[i]]+1
            else:
                hd[s[i]]=1
        for j in range(len(t)):
            if t[j] in hd:
                hd[t[j]]=hd[t[j]]-1
            if t[j] not in hd:
                return False
        for d in hd:
            if hd[d]!=0:
                return False
        
        return True

       

        




        