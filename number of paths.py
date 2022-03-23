class Solution:
    def numberOfPaths (self, n, m):
       if m == 1 or n == 1:
           return 1
       else:
           return self.numberOfPaths(n-1,m) + self.numberOfPaths(n,m-1)
