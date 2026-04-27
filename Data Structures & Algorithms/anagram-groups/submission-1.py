from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       li=[]
       hd={}
       for i in strs:
        std="".join(sorted(i))
        if std in hd:
            hd[std].append(i)
        else:
         hd[std]=[i]
        li=list(hd.values())
       return li
      
    





    