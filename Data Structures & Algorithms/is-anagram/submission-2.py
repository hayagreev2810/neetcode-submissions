class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic1 = {}

        for a in s:
            dic1[a] = dic1.get(a, 0) + 1

        for b in t:
            if b not in dic1:
                return False
            dic1[b] -= 1
            if dic1[b] < 0:
                return False

        return True