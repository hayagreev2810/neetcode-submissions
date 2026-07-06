class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hd={}
        li=[]
        for i in strs:
            std="".join(sorted(i))
            if std not in hd:
                hd[std]=[i]
            else:
                hd[std].append(i)
        li =list(hd.values())
        return li
            



           
                

        