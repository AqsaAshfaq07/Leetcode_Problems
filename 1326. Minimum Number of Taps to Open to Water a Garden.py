class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # garden -> 0 - n
        # n+1 taps located in the garden
        # n, ranges -> n+1 
        # ranges[i] -> ith tap can water the area - [i - ranges[i], i + ranges[i]]
        # return number of open taps to water the whole garden else - 1

        # n = 5, ranges = [3,4,1,1,0,0]
        # for i = 0 -> area = [-3, 3]
        # for i = 1 -> area = [-3, 5]
        # for i = 2 -> area = [1, 3]
        # for i = 3 -> area = [2, 4]
        # for i = 4 -> area = [4, 4]
        # for i = 5 -> area = [5, 5]

        inf = int(1e9)
        dp = [inf] * (n + 1)

        dp[0] = 0
        for i in range(n+1):
            tap_start = max(0, i-ranges[i])
            tap_end = min(n, i+ranges[i])

            for j in range(tap_start, tap_end+1):
                dp[tap_end] = min(dp[tap_end], dp[j] + 1)

        return dp[n] if dp[n] != inf else -1

# Time Complexity -> O(n^2)
# Space Complexity -> O(n)  