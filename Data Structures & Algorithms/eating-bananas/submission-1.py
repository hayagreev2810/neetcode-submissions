import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        ans = r

        while l <= r:

            m = l + (r - l) // 2

            hours_taken = 0

            for pile in piles:
                hours_taken += math.ceil(pile / m)

            if hours_taken <= h:
                ans = m
                r = m - 1

            else:
                l = m + 1

        return ans