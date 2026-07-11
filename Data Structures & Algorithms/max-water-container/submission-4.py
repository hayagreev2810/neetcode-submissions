"""
approach: 2 pointers

T.C. O(n)
S.C. O(1)
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        p1, p2 = 0, len(heights)-1

        while p1<p2:
            width = p2-p1
            height = min(heights[p1],heights[p2])
            currArea = width * height
            maxArea = max(maxArea, currArea)

            if heights[p1]<heights[p2]:
                p1+=1
            else:
                p2-=1
        
        return maxArea