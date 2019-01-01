class Solution:
    def minAddToMakeValid(self, S):
        chars=list(S)
        stack= list()
        count=0
        
        for char in chars:
            if char=='(':
                stack.append('(')
                
            else:
                if len(stack)!=0:
                    stack.pop()
                else:
                    count=count+1
                    
        return len(stack)+count 
        
