class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hd={}
        for i in nums:
            hd[i]=hd.get(i,0)+1
            if hd[i]>1: 
                return True
        return False
