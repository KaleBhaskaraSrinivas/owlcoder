class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        plat=1
        p=1
        q=0
        while p<n:
            if arr[p]>dep[q]:
                p+=1
                q+=1
            else:
                plat+=1
                p+=1
        return plat
