class Solution:

    def candyStore(self, candies,N,K):
        candies.sort()
        length=N
        low=high=0
        for i in range(length):
            low = low+candies[i]
            high = high+candies[length-i-1]
            N-=(1+K)
            if(N<=0):
                break
        return [low,high]
