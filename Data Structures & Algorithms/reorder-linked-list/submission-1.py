# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse right side of list
        curr2 = slow.next
        prev = None
        while curr2:
            nxt = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = nxt

        curr2 = slow.next
        slow.next = None

        left_curr = head
        right_curr = prev

        while left_curr and right_curr:
            nxt1 = left_curr.next
            nxt2 = right_curr.next

            left_curr.next = right_curr
            right_curr.next = nxt1

            left_curr = nxt1
            right_curr = nxt2
    




            
            
            






