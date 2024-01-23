class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        for i in range(3, n+1):
            c = a+b
            a = b
            b = c
        return a if n==1 else b

# Time -- O(n)
# Space -- O(1)
