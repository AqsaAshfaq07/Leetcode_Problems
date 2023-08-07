class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for _ in range(n + 1)] for _ in range(goal + 1)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, min(i, n) + 1):
                dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % mod
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % mod

        return dp[goal][n]



        # n -> total number of songs 
        # -> length of number of songs in each playlist
        # goal -> number of songs you wanna hear 
        # -> length of expected possible playlist 
        # k -> least number of songs you should hear before
        # repeating any other song
        #  return -> number of possible playlists
