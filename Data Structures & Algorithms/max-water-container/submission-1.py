class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        area=0
        maxarea=0
        while r>l:
            length=min(heights[r],heights[l])
            width=r-l
            area=length*width
            maxarea=max(maxarea,area)
            if(heights[r]>=heights[l]):
                l=l+1
            else:
                r=r-1
        return maxarea
     
     
       
        
