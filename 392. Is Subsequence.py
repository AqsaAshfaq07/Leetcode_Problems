class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:  
        n = len(s)
        if n == 0: return True 

        for i in range(len(t)):
            if t[i] == s[len(s) - n]:
                n -= 1
            if n == 0: return True
        if n > 0:
            return False
        