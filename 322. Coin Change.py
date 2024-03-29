class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        coins.sort()

        for i in range(1, amount + 1):
            for c in coins:
                if i - c < 0:
                    break
                if dp[i - c] != float('inf'):
                    dp[i] = min(dp[i], 1 + dp[i - c])

        return -1 if dp[amount] == float('inf') else dp[amount]

# Time -- O(n*m)
# Space -- O(n)
