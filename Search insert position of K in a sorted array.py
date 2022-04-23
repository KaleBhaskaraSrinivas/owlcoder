class Solution:
    def searchInsertK(self, Arr, N, k):
        r=0
        l=N-1
        while(r<=l):
            b=(r+l)//2
            if Arr[b]==k:
                return b
            elif Arr[b]<k:
                r+=1
            else:
                l-=1
        return r
    
    
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends
