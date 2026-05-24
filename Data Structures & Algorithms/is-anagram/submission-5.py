class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hd1={}
        hd2={}
        for i in s:
            hd1[i]=hd1.get(i,0)+1
        for j in t:
            if j not in hd1:
                return False
            else:
                hd1[j]=hd1.get(j,0)-1
                if hd1[j]<0:
                    return False
        for d in hd1:
            if hd1[d]!=0:
                return False
        return True
