class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        dic1={}
        dic2={}
        for a in s:
         if (a not in dic1):
          dic1[a]=1
         else:
          dic1[a]+=1

        for b in t:
          if (b not in dic2):
           dic2[b]=1
          else:
           dic2[b]+=1
          
        if dic1 == dic2:
          return True
        else:
         return False


        