class Solution:
    def duplicates(self, arr, n):
        duplicate={}
        val=[]
        for i in arr:
            if i not in duplicate:
                duplicate[i]='0'
            else:
                duplicate[i]='1'
        for i in duplicate:
            if  duplicate[i]=='1':
                val.append(i)
        if len(val) == 0:
            val.append(-1)
        val.sort()   
        return val
