class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
       low = 0
       high = N - 1
       
       while low <= high:
           mid = low +(high -low)//2
           if arr[mid] == K:
               return 1
           
           elif K < arr[mid]:
               high = mid -1
           
           else:
               low = mid + 1
       
       return -1
