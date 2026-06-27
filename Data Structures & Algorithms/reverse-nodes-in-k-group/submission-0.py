# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==1:
            return head
        
        dummy = ListNode(0,head)
        prev = dummy
        curr= head
        count = 0
        while curr:
            count+=1
            curr = curr.next
        
        while count>=k:
            curr = prev.next
            next_node = curr.next

            for _ in range(1,k):
                curr.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node
                next_node = curr.next
            prev = curr
            count-=k
        return dummy.next