class Solution:
    def gameOfXor(self, N , A):
        if N%2==0:
            return 0
        res=0
        for i in range(0,N,2):
              res=res^A[i]
        return res
