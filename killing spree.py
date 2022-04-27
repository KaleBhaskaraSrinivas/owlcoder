class Solution:
    def killinSpree (self, n):
        lo=1
        hi=n
        while lo<hi:
            mid=(lo+hi+1)>>1
            count=mid*(mid+1)*(2*mid+1)//6
            if count>n:
                hi=mid-1
            else:
                lo=mid
        return lo
