from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        counter,res, used = Counter(s), 0, set()
        for ch, freq in counter.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res

# Time Complexity -> O(n)
# Space Complexity -> O(n)
            