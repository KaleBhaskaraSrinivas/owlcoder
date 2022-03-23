class Solution:
    def nthFibonacci(self,n):
        l=[0,1]
        c=2
        i=2
        while(c<=n):
            l.append(l[i-1]+l[i-2])
            i+=1
            c+=1
        return l[n]%1000000007
