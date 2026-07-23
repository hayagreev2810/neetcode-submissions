class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=['+','-','*','/']
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            if i=='+':
                a=stack.pop()
                b=stack.pop()
                stack.append(int(a+b))
            if i=='-':
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b-a))
            if i=='*':
                 a=stack.pop()
                 b=stack.pop()
                 stack.append(int(a*b))
            if i=='/':
                 a=stack.pop()
                 b=stack.pop()
                 stack.append(int(b/a))
        return stack[0]
