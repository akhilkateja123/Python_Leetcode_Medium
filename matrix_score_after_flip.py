class Solution(object):
    def matrixScore(self, A):
        n= len(A)
        m=len(A[0])
        
        for i in range(n):
            A[i]= A[i] if A[i][0]==1 else [x^1 for x in A[i]]
        
        B=zip(*A)
        
        for i in range(m):
            B[i]=B[i] if B[i].count(1)>= (n+1)/2 else [x^1 for x in B[i]]
            
        return sum([int(''.join([str(num) for num in row]),2) for row in zip(*B)]) 
