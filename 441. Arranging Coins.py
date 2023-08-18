class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n 

        while left <= right:
            mid = (left + right) // 2 
            coins_req = mid * (mid + 1)  // 2  
            if curr == n:
                return mid
            elif curr > n:
                right = mid - 1
            else:
                left = mid + 1

        return right
