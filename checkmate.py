class Solution:
    def checkmate(self, a, b, x, y):
        if a==x or b==y:
            return(0)
        elif abs(a-x)==abs(b-y):
            return (0)
        else:
            return (1)
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        a, b, x, y= map(int,input().strip().split())
        ob = Solution()
        ans = ob.checkmate(a, b, x, y)
        if ans:
            print(1)
        else:
            print(0)


# } Driver Code Ends
