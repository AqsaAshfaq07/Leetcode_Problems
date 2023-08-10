class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)  # 5
        stack = []  # [ ]
        result = prices[:]  # [8, 4, 6, 2, 3]
        
        for i in range(n): # 1 -> 4
            while stack and prices[i] <= prices[stack[-1]]:
                j = stack.pop()
                result[j] -= prices[i]
            stack.append(i)
        
        return result

# Time Complexity -> O(n)
# Space Complexity -> O(n)  