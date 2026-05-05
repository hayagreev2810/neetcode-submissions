class Solution:
    def isValid(self, s: str) -> bool:
        hd={']':'[','}':'{',')':'('}
        stack=[]
        for i in s:
            if i in hd.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    x=stack.pop()
                    if x!=hd[i]:
                        return False
        return not stack
        