class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        c = 0
        a = set(a)
        b = set(b)
        h = {}
        for x in a:
            if x not in h:
                h[x] = 1 
        for i in b:
            if i in h:
                c += 1 
        return c
