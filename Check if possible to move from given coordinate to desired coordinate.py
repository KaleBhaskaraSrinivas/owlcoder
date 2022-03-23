import math
class Solution:
    def isPossible(self, x, y, a, b):
            if(math.gcd(a,b)==math.gcd(x,y)):
                return 1
            else:
                return 0
