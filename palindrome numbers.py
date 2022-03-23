class Solution:
    def isPallindrome(self, N):
        k=bin(N)
        k=k[2:]
        if k==k[::-1]:
            return 1
        else:
            return 0
        
