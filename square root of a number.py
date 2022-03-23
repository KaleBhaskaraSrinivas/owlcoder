class Solution:
    def floorSqrt(self, x):
        i=1
        result=1
        while(result<=x):
            i+=1
            result=i*i
        return i-1
