import numpy as np
class Solution:

    def MaxSum(self, A, B, N):
        A=np.sort(A)
        B=np.sort(B)
        return np.sum(A*B)
