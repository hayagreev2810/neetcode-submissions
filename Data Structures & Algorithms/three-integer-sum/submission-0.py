from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        for i in range(len(nums)):
            hash_dic = {}   # reset for each i
            
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                
                if target in hash_dic:
                    triplet = sorted([nums[i], nums[j], target])
                    
                    if triplet not in result:   # avoid duplicates
                        result.append(triplet)
                
                hash_dic[nums[j]] = j   # store value → index
        
        return result