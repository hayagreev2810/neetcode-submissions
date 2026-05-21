class Solution:
    def isValid(self, s: str) -> bool:
        hd={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if i not in hd:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                else:
                    a=stack.pop()
                    if(hd[i]!=a):
                        return False
        return not stack