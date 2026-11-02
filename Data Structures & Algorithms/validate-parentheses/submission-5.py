class Solution:
    def isValid(self, s: str) -> bool:
        
        p = {'(':')', '{':'}','[':']'}
        
        stack = []
        for i in s: 
            if i in p:
                stack.append(i)
            if i in p.values() and len(stack): 
                popped = stack.pop()
                if not p[popped] == i: 
                    return False
            elif i in p.values() and not len(stack): 
                return False

        return len(stack) == 0        
        