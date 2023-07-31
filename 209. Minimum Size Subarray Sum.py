class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        curr_sum, res = 0, float("inf")

        for end in .range(0, len(nums)):
            curr_sum += nums[end]

            while curr_sum >= target:
                res = min(res, end - start + 1)
                curr_sum -= nums[start]
                start += 1

        return res if res != float("inf") else 0


