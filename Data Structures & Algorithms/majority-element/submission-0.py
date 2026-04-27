class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hd={}
       
        for i in nums:
            if i in hd:
                hd[i]=hd[i]+1
            else:
                hd[i]=1
        for k,v in hd.items():
            if v>len(nums)//2:
                return k
            
        

