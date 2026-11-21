class Solution:
    def isPalindrome(self ,s:str)->bool:
        s=s.lower()
        s= ''.join(filter(str.isalnum,s))
        res_s=s[::-1]
        if s==res_s:
            return True
        else:
            return False

