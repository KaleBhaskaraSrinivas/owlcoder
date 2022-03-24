class Solution:
    def checkmate(self, a, b, x, y):
        if a==x or b==y:
            return(0)
        elif abs(a-x)==abs(b-y):
            return (0)
        else:
            return (1)
            
