class Solution:
    def reversedBits(self, X):
        s=""
        X=bin(X)
        x=X.replace("0b","")
        l=len(x)
        n=32-l
        for i in range(n):
           x="0"+x
        lis = list(x)
        lis.reverse()
        s=s.join(lis)
        r=int(s,2)
        return r
