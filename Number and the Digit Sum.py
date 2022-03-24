class Solution:
    def numberCount(self,n,k):
        rem=n%10
        digit=n-rem
        diff=digit-(digit%9)
        while diff>=k:
            digit=digit-10
            diff=digit-(digit%9)

        ans= n-digit+1-10
        if ans>0:
            return ans
        return 0
