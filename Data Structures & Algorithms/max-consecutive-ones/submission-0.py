class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum=0
        maximum=0
        for i in nums:
            if i==1:
                sum=sum+1
                maximum=max(sum,maximum)
            else:
                  
                  sum=0

                
                
        return maximum

