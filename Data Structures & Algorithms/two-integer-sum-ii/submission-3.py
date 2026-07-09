class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j=len(numbers)-1
        i=0
        while i<j:
            if(numbers[i]+numbers[j]==target):
                return[i+1,j+1]
            elif(i<j and numbers[i]+numbers[j]>target):
                j=j-1
            else:
                i=i+1