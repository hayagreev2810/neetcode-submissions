class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            if i== '+':
                b=stack.pop()
                a=stack.pop()
                stack.append(a+b)
            if i== '-':
                b=stack.pop()
                a=stack.pop()
                stack.append(a-b)
            if i== '*':
                b=int(stack.pop())
                a=int(stack.pop())
                stack.append(int(a*b))
            if i== '/':
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a/b))
        return stack[0]


      
        