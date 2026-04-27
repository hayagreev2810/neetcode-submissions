class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hd={}
        l=0
        longest_substring=0
        for i in range (len(s)):
            hd[s[i]]=hd.get(s[i],0)+1
            max_frequency=max(hd.values())
            wz=i-l+1
            replacable_characters=wz-max_frequency
            while(replacable_characters>k and l<len(s)):
                hd[s[l]]=hd.get(s[l],0)-1 
                l=l+1 
                max_frequency=max(hd.values())
                wz=i-l+1
                replacable_characters=wz-max_frequency
            
            longest_substring=max(longest_substring,wz)
        return longest_substring

                

       

          
            




