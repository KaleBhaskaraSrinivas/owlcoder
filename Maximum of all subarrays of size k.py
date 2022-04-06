class Solution:
    def max_of_subarrays(self,arr,n,k):
        ans=[]
        i=k
        j=0
        ans.append(max(arr[:k]))
        while i<n:
            if arr[j]==ans[-1]:
               ans.append(max(arr[j+1:i+1]))
            elif arr[i]>ans[-1]:
               ans.append(arr[i])
            else:
               ans.append(ans[-1])
            i+=1
            j+=1
        return ans
