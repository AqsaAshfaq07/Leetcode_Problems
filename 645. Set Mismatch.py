class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_expected = n * (n + 1) // 2
        sum_actual = sum(nums)
        sum_square_expected = n * (n + 1) * (2 * n + 1) // 6
        sum_square_actual = sum(x * x for x in nums)

        sum_difference = sum_expected - sum_actual
        square_sum_difference = sum_square_expected - sum_square_actual

        # Solving the two equations
        y_plus_x = square_sum_difference // sum_difference
        y_minus_x = sum_difference

        # Find the two numbers
        x = (y_plus_x - y_minus_x) // 2
        y = y_plus_x - x

        return [x, y]

# Time -- O(n)
# Space -- O(1)
