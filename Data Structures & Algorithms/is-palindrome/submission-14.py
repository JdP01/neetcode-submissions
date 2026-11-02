class Solution:
    def isPalindrome(self, s: str) -> bool:

        i=0
        j = len(s) -1
        s = s.lower()
        while i < len(s): 

            while i < len(s) and (i == ' ' or not s[i].isalnum()): 
                i += 1
            while j > 0 and (j == ' ' or not s[j].isalnum()): 
                j -= 1
            if i >= j:
                return True
            print (s[i], s[j])
            if s[i] != s[j]: 
                return False
            
            i +=1 
            j -=1

        return True