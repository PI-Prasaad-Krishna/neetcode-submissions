# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next is not None:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        if fast:
            curr = slow.next
            slow.next = None
        else:
            prev_slow.next = None
            curr = slow
        prev = None
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        first = head
        second = prev
        while second is not None:
            t1 = first.next
            t2 = second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2