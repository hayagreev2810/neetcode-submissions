class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_dic={}
        for i in nums:
            if i in hash_dic:
               return True
            else:
                hash_dic[i]=1
        return False