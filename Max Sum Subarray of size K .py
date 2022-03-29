class Solution:
    def maximumSumSubarray (self,K,Arr,N):
       s=0
       t=K
       for i in range(0,N):
           s=max(s,sum(Arr[i:t]))
           t+=1
       return s
