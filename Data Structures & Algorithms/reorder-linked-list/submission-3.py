# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next # start of node to reverse
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        left_curr = head
        right_curr = prev
        slow.next = None

        while left_curr and right_curr:
            nxt1, nxt2 = left_curr.next, right_curr.next

            left_curr.next = right_curr
            right_curr.next = nxt1

            left_curr = nxt1
            right_curr = nxt2


        
        """
        1 -> 2 -> None None <- 3 <- 4 <- 5
        ^
                                         ^
        """
        