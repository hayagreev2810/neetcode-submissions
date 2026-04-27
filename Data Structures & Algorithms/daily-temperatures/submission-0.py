class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        answer=[0]*n

        for i in range(n-1,-1,-1):
            while len(stack)>0 and  temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            if len(stack)==0:
                stack.append(i)
            if temperatures[stack[-1]]>temperatures[i]:
                answer[i]=stack[-1]-i
                stack.append(i)
         

        return answer