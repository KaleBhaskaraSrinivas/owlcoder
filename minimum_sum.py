class Solution:
    def solve(self, arr, n):
        # code here
        arr.sort()
        fir=0
        las=0
        for i in range(n):
            if i%2==0:
                fir=fir*10+arr[i]
            else:
                las=las*10+arr[i]
        return fir+las
           
