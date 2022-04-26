class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        stack = []
        for c in x:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif not stack or stack.pop() != c:
                return False
        return not stack
