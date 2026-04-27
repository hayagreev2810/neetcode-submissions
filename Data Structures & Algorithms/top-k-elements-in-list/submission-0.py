from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # Step 1: Build frequency map
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Sort by frequency (descending)
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Step 3: Take first k elements
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result