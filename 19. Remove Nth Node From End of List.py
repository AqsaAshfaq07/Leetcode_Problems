# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # either two pointers 
        # head = [1, 2], n = 1
        fast, slow = head, head # fast, slow = 1, 1

        for _ in range(n): fast = fast.next  # fast = 2
        if not fast: return head.next  # False
        while fast.next: fast, slow = fast.next, slow.next # False
        slow.next = slow.next.next # slow.next = Null

        return head
