# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # linked list 
        # split into k parts 
        # balanced sizes -> diff <= 1
        # decreasing order 
        # return array - k parts
# Intuition
        # result = [[_] * 3]
        # find linked list length -> n
        # parts -> n // k
        # outer for loop -> n
        # inner for loop -> parts -> add all elements in result[]
# Solution
        curr = head
        for N in range(1001):
            if not curr: break
            curr = curr.next
        width, remainder = divmod(N, k)

        ans = []
        curr = head
        for i in range(k):
            head = write = ListNode(None)
            for j in range(width + (i < remainder)):
                write.next = write = ListNode(curr.val)
                if curr: curr = curr.next
            ans.append(head.next)
        return ans

# Time Complexity -> O(n)
# Space Complexity -> O(k)
