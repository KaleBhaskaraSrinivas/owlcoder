class Solution:
    def stringPartition(ob,S,a,b):
        for i in range(1,len(S)):
           
           if int(S[:i])%a == 0 and int(S[i:])%b == 0:
               return S[:i] + " " + S[i:]
        return -1
