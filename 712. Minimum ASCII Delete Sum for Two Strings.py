class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        # Fill the dp array using dynamic programming
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))

        # The answer is in the bottom-right corner of the dp array
        return dp[len(s1)][len(s2)]

# Time Complexity -> O(m * n)
# Space Complexiy -> O(m * n)