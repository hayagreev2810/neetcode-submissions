class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs=set()
        l=0
        r=0
        longest=0
        while l<=r and r<len(s):
            if s[r] in hs:
                hs.remove(s[l])
                l=l+1
                length=(r-l)+1
                longest=max(length,longest)
            else:
                hs.add(s[r])
                length=(r-l)+1
                longest=max(length,longest)
                r=r+1
        return longest

        