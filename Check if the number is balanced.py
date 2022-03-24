class Solution:
	def balancedNumber(self, N):
	     n=str(N)
         mid=len(N)//2
         lhs=sum(map(int,n[:mid]))
         rhs=sum(map(int,n[mid+1:]))
         return lhs==rhs
