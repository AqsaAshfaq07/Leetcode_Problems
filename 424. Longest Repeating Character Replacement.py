class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_count = {}
        left = 0
        max_freq = 0

        for right in range(len(s)):
            freq_count[s[right]] = freq_count.get(s[right], 0) + 1
            max_freq = max(max_freq, freq_count[s[right]])
    
            if (right - left + 1) - max_freq > k:
                freq_count[s[left]] -= 1
                left += 1

        return (right - left + 1)


# Time Complexity -> O(n)
# Space Complexity -> O(k)