class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if not digits:
            return ans
        ans.append("")

        mapping = [" ", " ", "abc", "def", "ghi", "jkl", "mno",     "pqrs", "tuv", "wxyz"]
        
        for digit in digits:
            tmp = []
            for candidate in mapping[int(digit)]:
                for s in ans:
                    tmp.append(s + candidate)
            ans = tmp

        return ans
