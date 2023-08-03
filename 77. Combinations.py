class Solution:
    def combine(self, n, k):
        def backtrack(start, path):
            if len(path) == k:
                combinations.append(path[:])  # Append a copy of the current path
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        combinations = []
        backtrack(1, [])
        return combinations