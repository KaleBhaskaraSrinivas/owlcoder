class Solution:
    def merge(self, arr1, arr2, n, m):
        arr1.extend(arr2)
        arr1.sort()
        del arr2[:]
        for i in range(m):
            arr2.append(arr1[n+i])
        del arr1[n:]
