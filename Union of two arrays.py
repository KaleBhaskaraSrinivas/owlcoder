class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        set_a=set(a)
        set_b=set(b)
        return len(set_a.union(set_b))
