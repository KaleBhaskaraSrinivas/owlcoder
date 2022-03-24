class Solution:
    #Complete this function
    def power(self,N,R):
        M = 1000000007
        N %= M
        if R == 0:
            return 1
        if R == 1:
            return N
        tmp = self.power(N, R // 2)
        res = (tmp * tmp) % M
        if R % 2 != 0:
            res = (res * N) % M
        return res
