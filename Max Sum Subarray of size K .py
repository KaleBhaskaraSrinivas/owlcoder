class Solution:
    def maximumSumSubarray (self,K,Arr,N):
       s=0
       for i in range(0,N):
           s=max(s,sum(Arr[i:K]))
           K+=1
       return s
