class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: 
        dq = deque()
        result = []

        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)

        result.append(nums[dq[0]])

        for i in range(k, len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)
            result.append(nums[dq[0]])

        return result

        # max_window = []
        # for i in range(len(nums) - k + 1):
        #     window = nums[i : i + k]  
        #     max_window.append(max(window))

        # return max_window   -->> Results in Time Limit Exceed 

    
# Monotonic Deque - enables retrieval of elements from the end of the window

# Monotonic Data Structure - One in which elements are always sorted
# Decreasing queue - Elements are descending sorted
# Remove all elments less than x before adding x to the window to maintain the montonic decreasing property


