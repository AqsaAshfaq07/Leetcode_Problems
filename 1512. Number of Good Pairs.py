class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # nums - good pairs
        # if nums[i] == nums[j] 
        
        results = []
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if nums[i] == nums[j] and i < j:
                    results.append((i, j))

        return len(results)

# Time Complexity -> O(n^2)
# Space Complexity -> O(n)