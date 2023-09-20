class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        target = sum(nums) - x
        if target < 0: return -1

        max_len, curr_sum,left = -1, 0, 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                max_len = max(max_len, right-left+1)

        return len(nums) - max_len if max_len != -1 else -1
