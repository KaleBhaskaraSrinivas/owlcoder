class Solution:
    def farNumber(self,N,Arr):
        l=[]
        for i in range(N):
            pos=-1
            for j in range(N-1,i,-1):
               if Arr[j]<Arr[i]:
                   pos=j
                   break
            l.append(pos)
        return l
