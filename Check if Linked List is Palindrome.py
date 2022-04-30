class Solution:
    def isPalindrome(self, head):
        s=''
        a = head
        while a:
            s += str(a.data)
            a = a.next 
        
        return True if s == s[::-1] else False
