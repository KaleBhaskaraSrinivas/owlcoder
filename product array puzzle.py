class Solution:
    def productExceptSelf(self, nums, n):
        b = 1
        ans = []
        if not n:
            return ans 
        prod = [1]*n
        for i in range(n):
            prod[i] = b
            b*=nums[i]
            
        b = 1
        for i in range(n-1,-1,-1):
            prod[i] *= b
            b*=nums[i]
        
        return prod
