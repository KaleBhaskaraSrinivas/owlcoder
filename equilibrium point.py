class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        if N == 1:
            return 1
        l = 0
        r = sum(A)-A[0]
        i = 0
        while i < N - 1:
            if l == r:
                return i + 1
            l += A[i]
            r -= A[i + 1]
            i += 1
        return -1
            
