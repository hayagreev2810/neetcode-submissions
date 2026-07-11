class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        max_amount=0
        r=-1
        r=len(heights)-1
        while r>l :
            length=min(heights[r],heights[l])
            width=(r-l)
            amount=length*width
            max_amount= max(max_amount,amount)
            if heights[l]>=heights[r]:
                r-=1
            if heights[r]>heights[l]:
                l+=1
        return max_amount    





        