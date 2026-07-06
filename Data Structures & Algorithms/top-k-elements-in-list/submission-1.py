class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hd={}
        li=[]
        for i in nums:
            hd[i]=hd.get(i,0)+1
        
        sorted_data = sorted(hd.items(), key=lambda x: x[1], reverse=True)
        for i in range (k):
            li.append(sorted_data[i][0])
        return li
           
           

        

        

        