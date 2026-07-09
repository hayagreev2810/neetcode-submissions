class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        rm=1 
        lm=1
        for i in range(len(nums)):
            ans[i]=rm
            rm=rm*nums[i]
        for j in range(len(nums)-1,-1,-1):
            ans[j]=ans[j]*lm
            lm=lm*nums[j]
        return ans