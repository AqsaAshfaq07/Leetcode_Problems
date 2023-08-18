class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x  # 3, 2

        while left <= right:  # 3 <= 3
            mid = (left + right) // 2  # 3
            square = mid * mid  # 9

            if square == x:  # 9 == 8
                return mid
            elif square < x:  # 9 < 8
                left = mid + 1
            else:             # 9 > 8
                right = mid - 1

        return left - 1  # 2
