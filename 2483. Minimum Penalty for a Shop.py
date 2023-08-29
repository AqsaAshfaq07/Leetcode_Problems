class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # customer visit log -> customers -> 'N' and 'Y'
        # n = len(customers)
        # 0 < j < n
        # if (shop is open) and (ith hour -> 'N') -> penalty += 1
        # if (shop is closed) and (ith hour -> 'Y') -> penalty += 1

        n = len(customers)
        
        cur_penalty = min_penalty = customers.count('Y')
        earliest_hour = 0

        for i in range(n):
            if customers[i] == 'Y':
                cur_penalty -= 1
            else:
                cur_penalty += 1
            
            if cur_penalty < min_penalty:
                earliest_hour = i + 1
                min_penalty = cur_penalty

        return earliest_hour
        
             


