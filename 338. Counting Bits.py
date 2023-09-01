class Solution:
    def countBits(self, n: int) -> List[int]:
        # n , ans -> n + 1
        # 0 <= i <= n
        #     n = 5
            # get a number in i
            # bin_num = convert i to binary 
            # count 1's in it 

        ans = []
        for i in range(n+1):
            bin_num = bin(i)
            count = bin_num.count('1')
            ans.append(count)

        return ans



