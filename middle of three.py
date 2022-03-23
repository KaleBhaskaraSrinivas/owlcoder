class Solution:
    def middle(self,A,B,C):
        if ((A < B and B < C) or (C < B and B < A)) :
             return B;
        if ((B < A and A < C) or (C < A and A < B)) :
             return A;
        else :
             return C
