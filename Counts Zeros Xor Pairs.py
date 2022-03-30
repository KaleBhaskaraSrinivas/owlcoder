def calculate (arr, n) :
    c = 0
    for x in range(n):
        for y in range(x+1,n):
            if arr[x] ^ arr[y] == 0:
                c+=1
    return c
