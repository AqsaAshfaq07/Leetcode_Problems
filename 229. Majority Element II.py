class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        arr = list(set(nums))
        answers = []
        n = len(nums) // 3

        for element in arr:
            if nums.count(element) > n:
                answers.append(element)

        return answers