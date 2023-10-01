class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # string s -> remove characters 
        # "cbacdcbc"
        # stack = [a, c, d, b]

        stack = []
        last_occ = {}
        visited = set()

        for i in range(len(s)):  # O(n)
            last_occ[s[i]] = i

        for i in range(len(s)): # O(n)
            if s[i] not in visited:
                while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i ): 
                    visited.remove(stack.pop())

                stack.append(s[i])
                visited.add(s[i])

        return ''.join(stack)

# Time Complexity -> O(n)
# Space Complexity -> O(1)