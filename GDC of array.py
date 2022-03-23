class Solution:
    def gcd(self, n, arr):
        i=0
        res=arr[i]
        while(i<n):
            a=res
            b=arr[i]
            while(b):
                a,b=b,a%b
            res=a
            i+=1
        return res
