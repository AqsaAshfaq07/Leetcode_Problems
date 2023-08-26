# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

    # when modifying in-place 
    # swap corresponding values 
    # or -- store multiple values in the same pointer 
    
        if not head: return

        # get the mid of the linked list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next  # return mid
            fast = fast.next.next

        # reverse the second half of the linked list
        prev, curr = None, slow.next
        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        slow.next = None

        # Merge both halfs
        p1, p2 = head, prev
        while p2:
            temp = p1.next
            p1.next = p2
            p1 = p2
            p2 = temp
