import math
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1 
        r=max(piles)
        min_m=max(piles)+1
        while l<=r:
            m=(l+r)//2
            total_time=0
            for pile in piles:
                time_taken=ceil(pile/m)
                total_time+=time_taken
            if total_time>h:
                l=m+1
            if total_time<=h:
                r=m-1
                min_m=min(m,min_m)
        return min_m



        