class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # n pieces - colors - 'A' or 'B'
        # count the valid A and B values
        a = b = 0
        for i in range(1, len(colors) - 1):
            if colors[i-1] == colors[i] == colors[i+1]:
                if colors[i] == 'A': a += 1
                else: b += 1

        return a>b

# Time Complexity -> O(n)
# Space Complexity -> O(1)