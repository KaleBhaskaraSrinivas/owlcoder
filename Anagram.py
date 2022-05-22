class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        if len(a) != len(b):
            return False
        else:
            count = [0]*256
            for i in range(len(a)):
                count[ord(a[i])] +=1
                count[ord(b[i])] -=1
                
            if count == [0]*256:
                return True
            else: 
                return False
