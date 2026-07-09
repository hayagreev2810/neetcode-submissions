class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        right=[1]*len(nums)
        right[-1]=1
        lm=1
        rm=1
        ans=[]

        for i in range(len(nums)):
            left[i]=(lm)
            lm=lm*nums[i]
        for j in range(len(nums)-1,-1,-1):
            right[j]=rm
            rm=rm*nums[j]
        for k in range(len(nums)):
            ans.append(left[k]*right[k])
        return ans



