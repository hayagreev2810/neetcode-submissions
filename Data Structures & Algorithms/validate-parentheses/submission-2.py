class Solution:
    def isValid(self, s: str) -> bool:
        hd={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if i not in hd:
                stack.append(i)
            
            else:
                if not stack:
                    return False
                x=stack.pop()
                if hd[i]!=x:
                    return False
                
        return not stack