class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if not s or not t:
            return ""
        
        target_chars = Counter(t)  
        # target_chars = {"A" : 1, "B" : 1, "C" : 1}
        required_chars = len(target_chars)  # 3
        window_chars = {}
        formed_chars = 0 # 3
        left = 0 # 9
        min_len = float('inf') # 4
        min_window = ""  # "BANC" 
        
        for right in range(len(s)):   # 12
            char = s[right]   # "C"
            window_chars[char] = window_chars.get(char, 0) + 1  
            # window_chars = {"A" : 1, "D" : 0, "O" : 1, "B": 1, "E" : 0, "C" : 1 , "N" : 1}
            
            if char in target_chars and window_chars[char] == target_chars[char]:
                formed_chars += 1
            
            while formed_chars == required_chars and left <= right:
                current_len = right - left + 1  #  4
                
                if current_len < min_len:
                    min_len = current_len  # 4
                    min_window = s[left:right+1]  # "BANC"
                
                left_char = s[left] # B
                window_chars[left_char] -= 1 
                
                if left_char in target_chars and window_chars[left_char] < target_chars[left_char]:
                    formed_chars -= 1
                
                left += 1
        
        return min_window

# Time Complexity -> O(m)
# Space Complexity -> O(n + req_chars)