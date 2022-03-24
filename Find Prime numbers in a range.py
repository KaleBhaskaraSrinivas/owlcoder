class Solution:        
    def primeRange(self,M,N):
        c=[]
        for i in range(M,N+1):
            if i>1:
                s=int(math.sqrt(i))
                for j in range(2,s+1):
                    if i%j==0:
                        break
                else:
                    c.append(i)
        return c
