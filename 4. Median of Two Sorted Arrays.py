class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        for i in range(len(nums1)): nums3.append(nums1[i])
        for i in range(len(nums2)): nums3.append(nums2[i])
        nums3.sort()
        mid = len(nums3) // 2
        if len(nums3) %2 != 0: return nums3[mid]
        else: return (nums3[mid-1] + nums3[mid]) / 2

# Time Complexity -> O(n log n)
# Space Complexity -> O(n)