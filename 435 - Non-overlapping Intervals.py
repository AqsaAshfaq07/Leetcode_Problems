class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        ans, k = 0, float('-inf')

        for start, end in intervals:
            if start >= k:
                k = end
            else:
                ans += 1

        return ans

