
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


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,k = ( int(x) for x in input().split() )
        ob = Solution()
        print(ob.numberCount(n,k))
# } Driver Code Ends
