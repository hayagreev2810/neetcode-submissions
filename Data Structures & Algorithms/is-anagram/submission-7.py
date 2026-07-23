class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hd={}
        for i in s:
            hd[i]=hd.get(i,0)+1

        for j in t:
            if j not in hd:
                return False
            hd[j]=hd.get(j,1)-1
            if hd[j]<0:
                return False
        for d in hd:
            if hd[d]!=0:
                return False

        return True