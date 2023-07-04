class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # res = 0
        # for num in nums:
        #     if nums.count(num) == 1:
        #         res = num

        # return res

        return (3*sum(set(nums)) - sum(nums))//2 
        #  (3*5 - 9) // 2     ( 3 * 100 - 102) // 2