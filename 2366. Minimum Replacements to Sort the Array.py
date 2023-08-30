class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue
            # count how many elements are made from breaking nums[i]
            num_elements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]

            # Requires num_elements - 1 operations
            answer += num_elements - 1

            # Maximize nums[i] after replacement
            nums[i] = nums[i] // num_elements

        return answer

# Time Complexity -> O(n)
# Space Complexity -> O(1)