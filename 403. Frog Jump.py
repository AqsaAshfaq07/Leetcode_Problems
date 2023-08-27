class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # frog is crossing a river 
        # units - stone 
        # jump on the stone - avoid falling into water - 1 
        # Given 
        # positions of stones - ascending order -
        # Asked 
        # if frog can cross the river by stepping at the last stone
        # last jump - k -> next jump - k+1, k, k-1
        # Only jump in forward direction 
        # return if frog can cross the river 
        # [0, 1, 3, 5, 6, 8, 12, 17]

        n = len(stones)
        mark = {}
        dp = [[0] * 2001 for _ in range(n)]

        for i in range(n):
            mark[stones[i]] = i

        dp[0][0] = 1

        for idx in range(0, n):
            for prev_jump in range(0, n):
                if dp[idx][prev_jump]:
                    if stones[idx] + prev_jump in mark:
                        dp[mark[stones[idx] + prev_jump]][prev_jump] = 1
                    if stones[idx] + prev_jump + 1 in mark:
                        dp[mark[stones[idx] + prev_jump + 1]][prev_jump + 1] = 1
                    if prev_jump > 0 and stones[idx] + prev_jump - 1 in mark:
                        dp[mark[stones[idx] + prev_jump - 1]][prev_jump - 1] = 1
        for prev_jump in range(n + 1):
            if dp[n - 1][prev_jump]:
                return True
        
        return False

# Time Complexity -> O(n^2)
# Space Complexity -> O(n)