Intuition
Using Dynamic Programming to find the longest subsequence and keep track of the number of maximum length subsequences encountered.

Approach
Iterate through the nums array in a nested way to check if nums[j] < nums[i] and if it is so -> move on to the next conditions as mentioned in the code below

Complexity
Time complexity:
O(n^2)

Space complexity:
O(n)

Code
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lengths = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        count[i] = 0
                    if lengths[j] + 1 == lengths[i]:
                        count[i] += count[j]

        maxLength = max(lengths)
        res = 0
        
        for i in range(n):
            if lengths[i] == maxLength:
                res += count[i] 

        return res