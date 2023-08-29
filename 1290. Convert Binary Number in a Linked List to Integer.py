# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # head = 1 0 1  -> 5
        result = head.val  # 1
        while head.next:
            result = result * 2 + head.next.val  # 1, 2, 5
            head = head.next  # 1
        return result
