class Solution:
	def longSubarrWthSumDivByK (self,arr, n, K) :
	    maxLen = preSum = 0
        mods = [-1] + [-2]*K
        for i in range(n): 
            preSum = (preSum + arr[i]) % K
            preSum += K if preSum<0 else 0
            if (mods[preSum] != -2):
                maxLen = max(i - mods[preSum], maxLen)
            else: mods[preSum] = i
        return maxLen
