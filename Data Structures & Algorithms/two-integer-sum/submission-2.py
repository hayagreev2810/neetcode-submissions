class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hd={}
        for i in range(len(nums)):
            req=target-nums[i]
            if req in hd:
                return [hd[req],i]
            else:
                hd[nums[i]]=i

        