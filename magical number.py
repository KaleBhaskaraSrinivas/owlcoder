def binarySearch(arr,low,high):
    while low <= high:
       mid = low +(high-low)//2
       if mid == arr[mid]:
           return mid
       elif mid < arr[mid]:
           high = mid - 1
       else:
           low = mid + 1
    return -1
    
