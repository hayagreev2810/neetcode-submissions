from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = [False] * len(strs)
        result = []

        for i in range(len(strs)):
            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True

            for j in range(i + 1, len(strs)):
                if visited[j]:
                    continue

                if self.isAnagram(strs[i], strs[j]):
                    group.append(strs[j])
                    visited[j] = True

            result.append(group)

        return result

    def isAnagram(self, s1, s2):
        if len(s1) != len(s2):
            return False

        freq = {}

        for ch in s1:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in s2:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] < 0:
                return False

        return True