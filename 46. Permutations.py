class Solution:
    def permute(self, nums):
        def generate(n, nums):
            if len(nums) == 0:
                ans.append(path[:])  
                
            for i in range(len(nums)):
                x = nums.pop(i)
                path.append(x)
                generate(n - 1, nums)
                nums.insert(i, x)
                path.pop()

        ans = []
        path = []
        generate(len(nums), nums)
        return ans
