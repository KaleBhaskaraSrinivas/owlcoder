
def find(arr,n,x):
    fi= -1
    la= -1
    for i in range(0,n):
       if arr[i] == x:
           fi = i
           break
    for i in range(n-1,-1,-1):
       if arr[i] == x:
           la= i
           break
       
    return fi,la
