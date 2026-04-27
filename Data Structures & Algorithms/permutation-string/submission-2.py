class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hd1={}
        hd2={}
        l=0
        n1=len(s1)
        if len(s2)<len(s1):
            return False
        for i in s1:
            hd1[i]=hd1.get(i,0)+1
        for r in range(n1):
            hd2[s2[r]]=hd2.get(s2[r],0)+1
        if hd1==hd2:
            return True
        for r in range(n1,len(s2)):
            hd2[s2[l]]=hd2.get(s2[l],0)-1
            if hd2[s2[l]]==0:
                del hd2[s2[l]]
            l=l+1
            hd2[s2[r]]= hd2.get(s2[r],0)+1
           
            if hd1==hd2:
             return True
        return False