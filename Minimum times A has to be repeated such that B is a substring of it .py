class Solution:
    def minRepeats(self, A, B):
        y=A
        for i in range(1,10**3):
            if B in y:
                return i
            y+= A
        return -1
