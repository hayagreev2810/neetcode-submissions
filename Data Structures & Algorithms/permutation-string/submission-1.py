class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        l=0
        hd1={}
        hd2={ }
        if n1>n2:
            return False
        for i in s1:
            hd1[i]=hd1.get(i,0)+1
        for j in range(n1):
            hd2[s2[j]]=hd2.get(s2[j],0)+1
        if hd1==hd2:
            return True
        for k in range(n1,len(s2)):
            hd2[s2[l]]=hd2[s2[l]]-1    

            if hd2[s2[l]] == 0:
             del hd2[s2[l]]
            l=l+1
            hd2[s2[k]]= hd2.get(s2[k],0)+1
           
            if(hd1==hd2):
                return True
        return False


