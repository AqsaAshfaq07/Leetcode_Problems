class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(0, len(s)//2):
            string = s[0: i+1]
            length = len(s) // len(string)
            if string*length == s: return True
        return False459. Repeated Substring Pattern
