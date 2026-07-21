class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        li=[]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            if i!=0 and nums[i-1]==nums[i]:
                continue
            while l<r:
                add=nums[i]+nums[l]+nums[r]
                if add==0:
                    li.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                while l<r and add>0:
                    r=r-1
                    add=nums[i]+nums[l]+nums[r]

                while l<r and add<0:
                    l=l+1
                    add=nums[i]+nums[l]+nums[r]
        return li



        

        