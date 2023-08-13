class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        memo = {-1 : True}
        n = len(nums)

        def validSubarray(i):
            if i in memo: return memo[i] 
            ans = False

            if i > 0 and nums[i] == nums[ i - 1]: ans |= validSubarray(i - 2) 
            if i > 1 and nums[i] == nums[i - 1] == nums[ i - 2] : ans |= validSubarray(i - 3) 
            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2: ans |= validSubarray(i - 3)
            memo[i] = ans
            return ans

        return validSubarray(n - 1)