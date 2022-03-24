class Solution:
    def removeDuplicates(self, arr):
        # code here 
        s=[]
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
                s.append(i)
        return s
    
