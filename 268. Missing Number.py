class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sort array
        # if index != number : return index
        nums.sort() 
        n = len(nums) # 3
        for i in range(n):
            if i != nums[i]: 
                return i
        return n
        
# Time Complexity -> O(nlogn)
# Space Complexity -> O(1)